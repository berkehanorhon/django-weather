from django.contrib import admin
from .models import Location, QueryLog

admin.site.register(Location)
admin.site.register(QueryLog)