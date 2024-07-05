from rest_framework import serializers

class ConditionSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=100)
    icon = serializers.CharField(max_length=100)
    code = serializers.IntegerField()

class CurrentSerializer(serializers.Serializer):
    last_updated = serializers.CharField(max_length=100)
    condition = ConditionSerializer()
    wind_mph = serializers.FloatField()
    wind_kph = serializers.FloatField()
    wind_degree = serializers.IntegerField()
    wind_dir = serializers.CharField(max_length=10)
    pressure_mb = serializers.FloatField()
    pressure_in = serializers.FloatField()
    precip_mm = serializers.FloatField()
    precip_in = serializers.FloatField()
    humidity = serializers.IntegerField()
    cloud = serializers.IntegerField()
    feelslike_c = serializers.FloatField()
    feelslike_f = serializers.FloatField()
    windchill_c = serializers.FloatField()
    windchill_f = serializers.FloatField()
    heatindex_c = serializers.FloatField()
    heatindex_f = serializers.FloatField()
    dewpoint_c = serializers.FloatField()
    dewpoint_f = serializers.FloatField()
    vis_km = serializers.FloatField()
    vis_miles = serializers.FloatField()
    uv = serializers.FloatField()
    gust_mph = serializers.FloatField()
    gust_kph = serializers.FloatField()

class LocationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    region = serializers.CharField(max_length=100, allow_blank=True)
    country = serializers.CharField(max_length=100)
    lat = serializers.FloatField()
    lon = serializers.FloatField()
    tz_id = serializers.CharField(max_length=100)
    localtime_epoch = serializers.IntegerField()
    localtime = serializers.CharField(max_length=100)

class LocationInfoSerializer(serializers.Serializer):
    location = LocationSerializer()
    current = CurrentSerializer()
