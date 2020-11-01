from django.db import models
from django.conf import settings

# Create your models here.
class  Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content  = models.CharField(max_length=140)
    username = models.CharField(max_length=20, default=None)
    First_name = models.CharField(max_length=20, default=None)
    Last_name = models.CharField(max_length=20, default=None)

    def __str__(self):
        return str(self.content)