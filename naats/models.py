from django.db import models

# Create your models here.
class vidQualities(models.Model):
    id = models.IntegerField
    quality = models.CharField(max_length=10)

class vidTypes(models.Model):
    id = models.IntegerField
    type = models.CharField(max_length=10)

class naats(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=100)
    vidPath = models.CharField(max_length=200)
    imgPath = models.CharField(max_length=200)
    xDimension = models.SmallIntegerField
    yDimension = models.SmallIntegerField

    quality = models.ForeignKey(vidQualities, on_delete=models.CASCADE)
    type = models.ForeignKey(vidTypes, on_delete=models.CASCADE)

