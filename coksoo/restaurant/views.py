from rest_framework import viewsets
from rest_framework import permissions
from serializer import Type_of_mealSerializer, MealSerializer
from models import Type_of_meal, Meal
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework import status
from rest_framework.response import Response


class Type_of_mealViewSet(viewsets.ModelViewSet):
    queryset = Type_of_meal.objects.all()
    serializer_class = Type_of_mealSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        if request.user.type_of_user != 'Manager':
            return Response({'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST) 
        return Response({'message': 'You have created new type'}, status=status.HTTP_201_CREATED) 
    

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        if request.user.type_of_user != 'Manager':
            return Response({'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST) 
        return Response({'message': 'You have created new type'}, status=status.HTTP_201_CREATED) 