# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from appointment.models.models import Appointment
from appointment.serializers import AppointmentSerializer

class AppointmentListCreateView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check if the appointment slot is available
            date = serializer.validated_data['date']
            time_slot = serializer.validated_data['time_slot']
            if Appointment.objects.filter(date=date, time_slot=time_slot).exists():
                return Response({'error': 'Appointment slot already booked.'}, status=status.HTTP_400_BAD_REQUEST)
            # Create the appointment
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
