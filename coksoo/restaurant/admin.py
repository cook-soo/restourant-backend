from django.contrib import admin
from restaurant.models import Filial, Type_of_meal, Meal, Promocode
# Register your models here.

admin.site.register(Filial)
admin.site.register(Type_of_meal)
admin.site.register(Meal)
admin.site.register(Promocode)