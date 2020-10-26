from rest_framework import viewsets

from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer