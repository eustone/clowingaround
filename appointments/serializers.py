from rest_framework import serializers
from .models import Appointment,Review




class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            'user',
            'date',
            'time_start',
            'time_end',
            'appointment_with',
            'update_time',
            'first_time', )

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs ={
            'email': {'write_only':True}
        }
        model = Review
        fields = (
            'appointment',
            'name',
            'email',
            'comment',
            'rating',
            'created_at',
        )
