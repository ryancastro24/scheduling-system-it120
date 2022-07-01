
from django.db import models


class college(models.Model):
  collegeName = models.CharField(max_length=200)
  subject = models.CharField(max_length=200)
  numberOfUnits = models.CharField(max_length=200)
  timeAndDate = models.CharField(max_length=200)








