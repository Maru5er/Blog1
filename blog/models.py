from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=400)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_time = models.DateTimeField(default=timezone.now())
    published_time = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_time = timezone.now()
        self.save()

    def __str__(self):
        return self.title



