from django.db import models
# from user.models import Client, Courier, Cook
from restaurant.models import Meal


STATUSES = (
        (1, 'Option One'),
        (2, 'Option Two'),
        (3, 'Option Three'),
        # Add more choices as needed
    )



class Delivery(models.Model):
    date = models.DateField()
    address = models.CharField(max_length=600)
    comment = models.TextField()
    status = models.IntegerField(choices=STATUSES)
    number_of_foods = models.IntegerField(default=0)
    client = models.ForeignKey("user.Client", on_delete=models.CASCADE, related_name="client_delivery")
    courier = models.ForeignKey("user.Courier", on_delete=models.CASCADE, related_name="courier_delivery", null=True, blank=True)
    cook = models.ForeignKey("user.Cook", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        permissions = [
            ("change_cook_delivery", "Can change the cook of the delivery"),
        ]
        
    def increase_number_of_foods(self):
        self.number_of_foods+=1
        self.save()



class DeliveryMeal(models.Model):
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)