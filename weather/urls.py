from django.urls import path
from .views import get_location_info, get_all_locations, get_my_logs_api, get_my_logs

urlpatterns = [
    path('location/<int:location_id>/', get_location_info, name='get_location_info'),
    path('all_locations/', get_all_locations, name='get_all_locations'),
    path('get_my_logs/', get_my_logs_api, name='get_my_logs_api'),
]
