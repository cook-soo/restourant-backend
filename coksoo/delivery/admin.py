from django.contrib import admin
from delivery.models import Delivery, DeliveryMeal
from django import forms
from user.models import Cook

# Define a custom form for Cook users
class CookDeliveryAdminForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['cook']

class StandardDeliveryAdminForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

class DeliveryAdmin(admin.ModelAdmin):
    form = StandardDeliveryAdminForm

    def get_form(self, request, obj=None, **kwargs):
        if Cook.objects.filter(user=request.user).exists():
            return CookDeliveryAdminForm
        else:
            return StandardDeliveryAdminForm

    def has_change_permission(self, request, obj=None):
        if Cook.objects.filter(user=request.user).exists():
            return request.user.has_perm('delivery.change_cook_delivery')
        return super().has_change_permission(request, obj)

admin.site.register(Delivery, DeliveryAdmin)