import os
import uuid
import json
import base64
import urllib.request  # Import urllib to fetch JSON data
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from patient_dashboard.models.models import CNFT
from patient_dashboard.serializers import CNFTSerializer

class CNFTViewSet(viewsets.ModelViewSet):
    queryset = CNFT.objects.all()
    serializer_class = CNFTSerializer
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Generate unique token (UUID) for the CNFT
            token = uuid.uuid4()
            serializer.validated_data['token'] = token
            # Save the CNFT
            self.perform_create(serializer)
            
            # Convert the image data to base64 encoded string
            image_data_base64 = base64.b64encode(serializer.validated_data['image'].read()).decode('utf-8')
            
            # Fetch JSON data of the image from the API
            url = "http://127.0.0.1:8000/api/patient_dashboard/api/patient/cnft/"
            try:
                with urllib.request.urlopen(url) as response:
                    # Load the response as JSON
                    image_json_data = json.loads(response.read().decode())
                    # Check if the response is a list
                    if isinstance(image_json_data, list):
                        # Initialize an empty list to store image data from each item in the list
                        image_data_list = []
                        # Iterate over each item in the list
                        for item in image_json_data:
                            # Check if the item is a dictionary and contains the "image" key
                            if isinstance(item, dict) and "image" in item:
                                # Append the image data to the list
                                image_data_list.append(item["image"])
                        # Create a JSON object with the list of image data
                        image_data_json = {"imageData": image_data_list}
                    else:
                        # If the response is not a list, handle it accordingly
                        return Response({'error': "Invalid response format"}, status=500)
            except Exception as e:
                return Response({'error': str(e)}, status=500)
            
            #print("Image data JSON:", image_data_json)  # Debugging statement

            try:
                # Run yarn command with the specified script and pass image data as a command-line argument
                os.system(f"npx ts-node -r tsconfig-paths/register scripts/verboseCreateAndMint.ts '{json.dumps(image_data_json)}'")
            except Exception as e:
                # Handle error if needed
                return Response({'error': str(e)}, status=500)

            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
