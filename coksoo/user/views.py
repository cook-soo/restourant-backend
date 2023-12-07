from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from user.permissions import IsManager
from user.serializer import ClientSerializer, UserSerializer, ManagerSerializer, CourierSerializer
from user.models import Client, User, Manager, Courier
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate


def method_permission_classes(*classes):
    def decorator(func):
        def decorated_func(self, *args, **kwargs):
            self.permission_classes = classes
            self.check_permissions(self.request)
            return func(self, *args, **kwargs)
        return decorated_func
    return decorator


def serialize(request, fields: list[str], serializer):
    context = {"request": request}
    data = {field : request.data.get(field, "") for field in fields}
    return serializer(data=data, context=context)


def login(self, request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"Message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    authenticated_user = authenticate(request, username=username, password=password)
    if authenticated_user is not None:
        tokens = RefreshToken.for_user(user)
        return Response({'access_token': str(tokens.access_token),
                        'refresh_token': str(tokens)},
                        status=status.HTTP_200_OK)
    return Response({"Message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )        

    def create(self, request):
        user_fields = ["username", "first_name", "last_name", "password"]
        user_ser = serialize(request, user_fields, UserSerializer)
        if user_ser.is_valid():
            return Response({"fields": user_ser.validated_data}, status=status.HTTP_200_OK)
        return Response(user_ser.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'])
    def login_user(self, request):
        login(self, request)
        pass


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (AllowAny, )
    
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
    permission_classes = (IsAuthenticated, )
    
    @method_permission_classes(IsAdminUser)
    def create(self, request):
        response = UserViewSet().create(request=request)
        if status.is_server_error(response.status_code): return response

        user = User.objects.create_user(**response.data["fields"])
        Manager.objects.create(user=user)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    permission_classes = (IsAuthenticated, )
    
    @method_permission_classes(IsManager)
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