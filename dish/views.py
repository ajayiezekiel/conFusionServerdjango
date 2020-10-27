from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Dish
from .serializers import DishSerializer

class DishViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

# class DishList(generics.ListCreateAPIView):
#     queryset = Dish.objects.all()
#     serializer_class = DishSerializer
#     name = 'dish-list'


# class DishDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Dish.objects.all()
#     serializer_class = DishSerializer
#     name = 'dish-detail'

# class ApiRoot(generics.GenericAPIView):
#     name = 'api-root'
    
#     def get(self, request, *args, **kwargs):
#         return Response({
#             'dishes': reverse(DishList.name, request=request)
#             })