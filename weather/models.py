from django.db import models
from django.utils import timezone
from django.conf import settings

class Location(models.Model):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

class QueryLog(models.Model):
    STATUS_CHOICES = (
        ('SUCCESS', 'Başarılı'),
        ('FAILURE', 'Başarısız'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='query_logs')
    query_time = models.DateTimeField(default=timezone.now)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='query_logs')
    user_ip = models.GenericIPAddressField()
    query_result = models.TextField()
    query_duration = models.IntegerField()
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user} - {self.location.name} - {self.query_time} - {self.status}"
