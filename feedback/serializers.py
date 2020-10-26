from rest_framework import serializers

from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'firstname', 'lastname', 'telnum', 'email', 'agree', 'contactType', 'message']

