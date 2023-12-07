from django.db import models
from user.models import Client, Courier, Cook
from restaurant.models import Meal


class Delivery(models.Model):
    date = models.DateField()
    address = models.CharField(max_length=600)
    comment = models.TextField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_delivery")
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE, related_name="courier_delivery", null=True)
    cook = models.ForeignKey(Cook, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user


class DeliveryMeal(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)