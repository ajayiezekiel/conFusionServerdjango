from rest_framework import serializers

from .models import Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'image', 'category', 'featured', 'label', 'price', 'description', 'comments']
