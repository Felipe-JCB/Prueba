from django.db import models

# Create your models here.
class Json(models.Model):
    devicename = models.TextField()
    averagebefore = models.TextField()
    averageafter = models.TextField()
    datasize = models.TextField()
    rawdata = models.TextField()