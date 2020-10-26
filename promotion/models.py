from django.db import models

# Create your models here.

class Promotion(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    featured = models.BooleanField()
    label = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name