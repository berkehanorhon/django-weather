from django.urls import path
from .views import get_location_info

urlpatterns = [
    path('location/<int:location_id>/', get_location_info, name='get_location_info'),
]
