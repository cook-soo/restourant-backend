from rest_framework import permissions
from rest_framework import viewsets
from delivery.models import Delivery, DeliveryMeal
from delivery.serializers import DeliverySerializer, DeliveryMealSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_permissions(self):
    #     # Bypass permissions for schema generation
    #     if self.action == 'metadata':
    #         return []
    #     return [permission() for permission in self.permission_classes]

class DeliveryMealViewSet(viewsets.ModelViewSet):
    queryset = DeliveryMeal.objects.all()
    serializer_class = DeliveryMealSerializer
    permission_classes = [permissions.IsAuthenticated]
