from django.db import models
from user.models import User


class Delivery(models.Model):
    date = models.DateField()
    address = models.CharField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_delivery")

    def __str__(self):
        return self.user