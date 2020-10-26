from django.db import models

# Create your models here.

class Feedback(models.Model):
    STATUS_CHOICES = (
        ('none', 'None'),
        ('email', 'Email'),
        ('tel', 'Tel'),
        )

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    telnum = models.PositiveIntegerField()
    email = models.EmailField()
    agree = models.BooleanField()
    contactType = models.CharField(choices=STATUS_CHOICES, max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.firstname


