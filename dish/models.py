from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=100)
    featured = models.BooleanField()
    label = models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Comment(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=80)
    comment = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author} on {self.dish.name}'



