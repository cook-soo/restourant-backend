from django.db import models
# from user.models import Client, Courier, Cook
from restaurant.models import Meal


class Delivery(models.Model):
    date = models.DateField()
    address = models.CharField(max_length=600)
    comment = models.TextField()
    client = models.ForeignKey("user.Client", on_delete=models.CASCADE, related_name="client_delivery")
    courier = models.ForeignKey("user.Courier", on_delete=models.CASCADE, related_name="courier_delivery", null=True, blank=True)
    cook = models.ForeignKey("user.Cook", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        permissions = [
            ("change_cook_delivery", "Can change the cook of the delivery"),
        ]



class DeliveryMeal(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)