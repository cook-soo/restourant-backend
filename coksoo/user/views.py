from rest_framework import viewsets
from rest_framework import permissions
from user.serializer import ClientSerializer, UserSerializer, ManagerSerializer, CourierSerializer
from user.models import Client, User, Manager, Courier
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request

def serialize(request, fields: list[str], serializer):
    context = {"request": request}
    data = {field : request.data.get(field, "") for field in fields}
    return serializer(data=data, context=context)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]        

    def create(self, request):
        user_fields = ["username", "first_name", "last_name", "password"]
        user_ser = serialize(request, user_fields, UserSerializer)
        if user_ser.is_valid():
            return Response({"fields": user_ser.validated_data}, status=status.HTTP_200_OK)
        return Response(user_ser.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        response = UserViewSet().create(request=request)
        if status.is_server_error(response.status_code): return response

        client_fields = ["phonenumber", "address"]
        client_ser = serialize(request, client_fields, ClientSerializer)
        if not client_ser.is_valid():
            return Response(client_ser.errors, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(**response.data["fields"])
        Client.objects.create(user=user, **client_ser.validated_data)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        response = UserViewSet().create(request=request)
        if status.is_server_error(response.status_code): return response

        user = User.objects.create_user(**response.data["fields"])
        Manager.objects.create(user=user)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request):
        response = UserViewSet().create(request=request)
        if status.is_server_error(response.status_code): return response

        courier_fields = ["phonenumber"]
        courier_ser = serialize(request, courier_fields, CourierSerializer)
        if not courier_ser.is_valid():
            return Response(courier_ser.errors, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(**response.data["fields"])
        Courier.objects.create(user=user, **courier_ser.validated_data)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]
    
    