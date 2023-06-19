from django.db import transaction
from rest_framework.exceptions import ValidationError



def transaction_handler(func, data=dict(), e=ValidationError):
	try:
		with transaction.atomic():
			return func(data)
	except:
		raise e()
