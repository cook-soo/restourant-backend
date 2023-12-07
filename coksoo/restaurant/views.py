from rest_framework import viewsets
from rest_framework import permissions
from serializer import Type_of_mealSerializer, MealSerializer
from models import Type_of_meal, Meal
from rest_framework import status
from rest_framework.response import Response
from restaurant.permissions import IsManager

def method_permission_classes(*classes):
    def decorator(func):
        def decorated_func(self, *args, **kwargs):
            self.permission_classes = classes
            self.check_permissions(self.request)
            return func(self, *args, **kwargs)
        return decorated_func
    return decorator


class Type_of_mealViewSet(viewsets.ModelViewSet):
    queryset = Type_of_meal.objects.all()
    serializer_class = Type_of_mealSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]
    

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated, IsManager]