from django.db import models

# Create your models here.
class User(models.Model):
  user = models.CharField(max_length=25, null=False)
  password = models.CharField(max_length=30, null=False)