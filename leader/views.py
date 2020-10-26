from rest_framework import viewsets

from .models import Leader
from .serializers import LeaderSerializer

class LeaderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer