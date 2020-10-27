from rest_framework import serializers

from .models import Dish, Comment

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'rating', 'comment', 'date']

class DishSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Dish
        fields = ['url', 'id', 'name', 'image', 'category', 'featured', 'label', 'price', 'description', 'comments']


