from django.contrib import admin
from delivery.models import Delivery, DeliveryMeal
from django import forms
from user.models import Cook


class DeliveryAdminForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['cook']

class DeliveryAdmin(admin.ModelAdmin):
    form = DeliveryAdminForm

    def get_form(self, request, obj=None, **kwargs):
        if Cook.objects.filter(user=request.user).exists():
            return DeliveryAdminForm
        else:
            return super().get_form(request, obj, **kwargs)

    def has_change_permission(self, request, obj=None):
        if obj is not None and Cook.objects.filter(user=request.user).exists():
            return request.user.has_perm('delivery.change_cook_delivery')
        return super().has_change_permission(request, obj)


admin.site.register(Delivery, DeliveryAdmin)
# admin.site.register(Delivery)