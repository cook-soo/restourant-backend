from django.contrib import admin
from django import forms
from user.models import User, Courier, Client, Manager, Cook

# admin.site.register(User)
admin.site.register(Client)
admin.site.register(Manager)
admin.site.register(Courier)
admin.site.register(Cook)