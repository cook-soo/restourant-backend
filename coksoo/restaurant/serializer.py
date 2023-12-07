from rest_framework import serializers
from restaurant.models import Type_of_meal, Meal, Promocode, Filial


class FilialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Filial
        fields = ['url', 'id', 'address']


class Type_of_mealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type_of_meal
        fields = ['url', 'id', 'name', 'description']
        

class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meal
        fields = ['url', 'id', 'name', 'price', 'description', 'type_of_meal']
        

class PromocodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Promocode
        fields = ['url', 'id', 'value', 'expiry_date']