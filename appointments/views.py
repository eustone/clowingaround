
from rest_framework import generics

from.models import Appointment,Review
from .serializers import AppointmentSerializer,ReviewSerializer



# Create your views here.

class ListCreateAppointment(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class RetrieveUpdateDestroyAppointment(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class ListCreateReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RetrieveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



