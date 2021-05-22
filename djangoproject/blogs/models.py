from django.db import models

# Create your models here.
class dataDoctor(models.Model):
    name=models.CharField(max_length=200)
    expertise=models.TextField()
    imageUrl=models.TextField()

class Disease(models.Model):
    name=models.CharField(max_length=200)
    imageUrl=models.TextField()
    information=models.TextField()