from django.db import models
from django.conf import settings

# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.DO_NOTHING)
    date = models.CharField(max_length=50)
    time_start = models.CharField(max_length=50)
    time_end = models.CharField(max_length=50)
    appointment_with = models.CharField(max_length=50, blank=True)
    update_time = models.DateField(auto_now=True, auto_now_add=False)
    first_time = models.DateField(auto_now=False, auto_now_add=True)

    # show filed in admin panel
    def __str__(self):
        return self.date


class Review(models.Model):
    appointment = models.ForeignKey(Appointment,on_delete=True, related_name='reviews')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['email', 'appointment']

    def __str__(self):
        return '{0.rating} by {0.email} for {0.appointment}'.format(self)



