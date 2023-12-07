from django.db.models import *
from django.contrib.auth.models import User
from restaurant.models import Filial

    
class UserType(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    
    def __str__(self):
        return self.user
        
    class Meta:
        abstract = True


class Client(UserType):
    phonenumber = CharField(max_length=100)
    address = CharField(max_length=100)
    
    def __str__(self):
        return f"Client {super()}"
    
    
class Manager(UserType):
    def __str__(self):
        return f"Manager {super()}"
    
    
class Courier(UserType):
    phonenumber = CharField(max_length=100)

    def __str__(self):
        return f"Courier {super()}"
    

class Cook(UserType):
    filial = ForeignKey(Filial, on_delete=CASCADE, related_name="cook_filial")
    qr_code = ImageField()    
    
    def __str__(self):
        return f"Cook {super()}"