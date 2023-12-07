from django.db import models


class Filial(models.Model):
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address


class Type_of_meal(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=400)
    price = models.IntegerField(default=0)
    description = models.TextField()
    type_of_meal = models.ForeignKey(Type_of_meal, on_delete=models.CASCADE, related_name='meal_type')

    def __str__(self):
        return self.name


class Promocode(models.Model):
    value = models.CharField(max_length=20)

    def __str__(self):
        return self.value