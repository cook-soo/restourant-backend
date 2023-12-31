from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from user.models import Client, Manager, Courier, User, Cook


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'password')

class UserTypeSerializer(HyperlinkedModelSerializer):
    username = SerializerMethodField()
    first_name = SerializerMethodField()
    last_name = SerializerMethodField()
    
    class Meta:
        abstract = True
            
    def get_username(self, obj):
        return obj.user.username
    
    def get_first_name(self, obj):
        return obj.user.first_name
    
    def get_last_name(self, obj):
        return obj.user.last_name


class ClientSerializer(UserTypeSerializer):
    class Meta:
        model = Client
        fields = ('url', 'id', 'phonenumber', 'address','username', 'first_name', 'last_name', 'bonuses')


class ManagerSerializer(UserTypeSerializer):
    class Meta:
        model = Manager
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'bonuses')


class CourierSerializer(UserTypeSerializer):
    class Meta:
        model = Courier
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'phonenumber', 'bonuses')


class CookSerializer(UserTypeSerializer):
    class Meta:
        model = Cook
        fields = ('url', 'id', 'username', 'first_name', 'last_name', 'filial', 'bonuses')