from django.db.models import *
from django.contrib.auth.models import User, Permission
from restaurant.models import Filial
from django.contrib.contenttypes.models import ContentType
from delivery.models import Delivery


    
class UserType(Model):
    bonuses = PositiveIntegerField(default=0)
    user = ForeignKey(User, on_delete=CASCADE)
    
    def __str__(self):
        return self.user
    
    def increase_bonuses(self, amount):
        self.bonuses += amount*0.05
        self.save()
        
    def decrease_bonuses(self, amount):
        if self.bonuses-amount>0:
            self.bonuses-=amount
            self.save()
        
    class Meta:
        abstract = True


class Client(UserType):
    phonenumber = CharField(max_length=100)
    address = CharField(max_length=100)
    
    def __str__(self):
        return f"Client {self.user}"
    
    
class Manager(UserType):
    def __str__(self):
        return f"Manager {self.user}"

    
class Courier(UserType):
    phonenumber = CharField(max_length=100)

    def __str__(self):
        return f"Courier {self.user}"
    

class Cook(UserType):
    filial = ForeignKey(Filial, on_delete=CASCADE, related_name="cook_filial")
    
    def __str__(self):
        return f"Cook {self.user}"
    
    def save(self, *args, **kwargs):
        self.user.is_staff = True
        self.user.save()
        content_type = ContentType.objects.get_for_model(Delivery)
        permission = Permission.objects.get_or_create(
            codename='change_cook_delivery',
            name='Can change the cook of the delivery',
            content_type=content_type,
        )

        self.user.user_permissions.add(permission)