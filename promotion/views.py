from rest_framework import viewsets

from .models import Promotion
from .serializers import PromotionSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer