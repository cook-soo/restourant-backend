from rest_framework import serializers
from models import Delivery

class DeliverySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Delivery
        fields = ['url', 'id', 'date', 'location', 'user']