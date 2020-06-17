from django.db import models

# Create your models here.
class bootcamp_candidate(models.Model):
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    email=models.EmailField
