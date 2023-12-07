from rest_framework import viewsets
from rest_framework import permissions
from restaurant.serializer import Type_of_mealSerializer, MealSerializer, FilialSerializer, PromocodeSerializer
from restaurant.models import Type_of_meal, Meal, Filial, Promocode
from rest_framework import status
from rest_framework.response import Response
from restaurant.permissions import IsManager


class FilialViewSet(viewsets.ModelViewSet):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]


class Type_of_mealViewSet(viewsets.ModelViewSet):
    queryset = Type_of_meal.objects.all()
    serializer_class = Type_of_mealSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]
    

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]
    

class PromocodeViewSet(viewsets.ModelViewSet):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]