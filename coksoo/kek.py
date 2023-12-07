from django.contrib.auth.models import User, Permission

# Assuming you have a Cook user's username
username = 'cook_username'
user = User.objects.get(username=username)

# Check if the user has the permission
permission = Permission.objects.get(codename='change_cook_delivery')
print(permission in user.user_permissions.all())  # Should be True
