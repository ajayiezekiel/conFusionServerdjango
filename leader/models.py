from django.db import models

# Create your models here.

class Leader(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    designation = models.CharField(max_length=100)
    abbr = models.CharField(max_length=50)
    featured = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return self.name

