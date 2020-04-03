from django.urls import include,path
from .views import ListCreateAppointment,RetrieveUpdateDestroyAppointment,ListCreateReview,RetrieveUpdateDestroyReview

app_name = 'appointments'

urlpatterns = [
   path('', ListCreateAppointment.as_view(), name='appointment_list'),
   path('<pk>', RetrieveUpdateDestroyAppointment.as_view(), name='appointment_detail'),
   path('', ListCreateReview.as_view(), name='review_list'),
   path('<pk>', RetrieveUpdateDestroyReview.as_view(), name='review_detail'),
]