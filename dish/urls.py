from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'dishes', views.DishViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path(r'^dishes/$', views.DishList.as_view(), name=views.DishList.name),
#     path(r'^dishes/(?P<pk>[0-9]+)$', views.DishDetail.as_view(), name=views.DishDetail.name),
# ]