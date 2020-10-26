from rest_framework import viewsets

from .models import Dish
from .serializers import DishSerializer

class DishViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer