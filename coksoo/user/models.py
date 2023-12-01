from django.db.models import *
from django.contrib.auth.models import User

    
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