"""
URL configuration for coksoo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.views.generic import TemplateView
from user.views import UserViewSet, ClientViewSet, ManagerViewSet, CourierViewSet
from restaurant.views import FilialViewSet, Type_of_mealViewSet, MealViewSet, PromocodeViewSet
from delivery.views import DeliveryViewSet, DeliveryMealViewSet
from rest_framework.schemas import get_schema_view



router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'client', ClientViewSet)
router.register(r'manager', ManagerViewSet)
router.register(r'courier', CourierViewSet)
router.register(r'filial', FilialViewSet)
router.register(r'type_of_meal', Type_of_mealViewSet)
router.register(r'meal', MealViewSet)
router.register(r'promocode', PromocodeViewSet)
router.register(r'delivery', DeliveryViewSet)
router.register(r'delivery_meal', DeliveryMealViewSet)



urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('documentation/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
            title="Coksoo",
            description="API for all things …",
            version="1.0.0"
    ), name='openapi-schema'),
]
