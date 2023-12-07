from rest_framework import serializers
from delivery.models import Delivery, DeliveryMeal

class DeliverySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Delivery
        fields = ['url', 'id', 'date', 'address', 'comment', 
                  'status', 'number_of_foods', 'client', 'courier', 'cook']
        

class DeliveryMealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeliveryMeal
        fields = ['url', 'id', 'delivery', 'meal']    