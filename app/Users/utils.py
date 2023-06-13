from .models import User



def get_user_by_username_or_email(data):
	if 'username' in data and data.get('username') != '-':
		return User.objects.get(username=data.get('username'))
	return User.objects.get(email=data.get('email'))