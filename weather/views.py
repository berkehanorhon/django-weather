import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Location
from .serializers import LocationInfoSerializer
from django.shortcuts import render, redirect

@api_view(['GET'])
def get_location_info(request, location_id):
    """
    Get given location's weather information.
    """
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
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Location.DoesNotExist:
        return Response({'error': 'Location not found'}, status=status.HTTP_404_NOT_FOUND)
    except requests.RequestException as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def get_weather_info(request, location_id):
    context = {
        'location_id': location_id
    }
    return render(request, 'weather/weather_info.html', context=context)
