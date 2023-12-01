from django.db import models


class Type_of_meal(models.Model):
    name = models.CharField(max_length=400)
    
    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()
    type_of_meal = models.ForeignKey(Type_of_meal, on_delete=models.CASCADE, related_name='meal_type')
    
    def __str__(self):
        return self.name