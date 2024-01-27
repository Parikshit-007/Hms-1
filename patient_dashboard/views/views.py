import subprocess
import uuid
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
            
            # Run TypeScript script using node directly
            script_path = "compressed-nfts/scripts/index.js"
            
            subprocess.run(["node", "--experimental-modules", script_path])
            
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
