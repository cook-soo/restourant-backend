from rest_framework import serializers
from models import Type_of_meal, Meal, Promocode, Filial


class FilialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Filial
        fields = ['url', 'address']


class Type_of_mealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type_of_meal
        fields = ['url', 'id', 'name']
        

class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meal
        fields = ['url', 'id', 'name']