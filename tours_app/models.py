from django.db import models


# Create your models here.
class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, default='')
    duration = models.IntegerField()
    maxGroupSize = models.IntegerField(blank=False)
    difficulty = models.CharField(max_length=50, blank=False)
    ratings = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    price = models.DecimalField(max_digits=50, decimal_places=2, default=0)
    description = models.CharField(max_length=500, default='')
