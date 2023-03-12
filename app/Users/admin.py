from django.contrib import admin
from .models import User



@admin.register(User)
class PersonAdmin(admin.ModelAdmin):
    fields = ('password', 'last_login', 'groups', 'user_permissions',
    	'email', 'username', 'last_name', 'first_name',
    	'is_staff', 'is_superuser', 'is_active')