import requests
from django.conf import settings
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from .models import Location, QueryLog
from .serializers import LocationInfoSerializer
from django.shortcuts import render, redirect
from django.http import JsonResponse
import time

@login_required
@api_view(['GET'])
def get_location_info(request, location_id):
    """
    Get given location's weather information.
    """
    start = time.time()
    QueryLogEntity = QueryLog.objects.create(user=request.user, location_id=location_id,
                                       user_ip=request.META.get('REMOTE_ADDR'))
    try:
        location = Location.objects.get(id=location_id)
        location_name = location.name

        api_url = f'https://api.weatherapi.com/v1/current.json?key={settings.EXTERNAL_API_KEY}&lang=tr&q={location_name.lower()}'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            return Response({'error': "There was an error while trying to get information from external api."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        serializer = LocationInfoSerializer(data=data)

        if serializer.is_valid():
            QueryLogEntity.status = 'SUCCESS'
            QueryLogEntity.query_result = f'Temperatures: {serializer.data["current"]["heatindex_c"]} °C / {serializer.data["current"]["heatindex_f"]} °F'
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Location.DoesNotExist:
        return Response({'error': 'Location not found'}, status=status.HTTP_404_NOT_FOUND)
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        QueryLogEntity.query_duration = time.time() - start
        QueryLogEntity.save()

@api_view(['GET'])
@login_required
def get_all_locations(request):
    locations = Location.objects.all().values('id', 'name')
    locations_list = list(locations)
    return JsonResponse(locations_list, safe=False)

@api_view(['GET'])
@login_required
def get_my_logs_api(request):
    logs = QueryLog.objects.filter(user=request.user).values('location__name', 'query_time', 'user_ip', 'query_result', 'query_duration', 'status').order_by('-query_time')
    logs_list = list(logs)
    return JsonResponse(logs_list, safe=False)

@login_required
def get_weather_info(request):
    return render(request, 'weather/weather_info.html')

def get_my_logs(request):
    return render(request, 'weather/my_logs.html')
