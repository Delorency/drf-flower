from django.db import models
from django.core import validators
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(validators=[validators.EmailValidator],
		unique=True, verbose_name='Email')

	username = models.CharField(max_length=100, verbose_name='Username')

	last_name = models.CharField(max_length=100, verbose_name='Last name')
	first_name = models.CharField(max_length=100, verbose_name='First name')

	created_at = models.DateTimeField(auto_now_add=True,
		verbose_name='Created at')
	updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

	is_private = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ('username', 'last_name', 'first_name')

	objects = UserManager()

	def __str__(self):
		return f'id:{self.id} | first_name:{self.first_name} | \
		email:{self.email}'


	class Meta:
		unique_together = ('username', 'is_active')
		verbose_name_plural = 'Users'
		verbose_name = 'User'
		ordering = ['-created_at']