from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import get_user_model, logout
import re

# Create your views here.


def index(request):	
	return render(request, 'adminTemplates/login/login.html')


def login(request):
	username = request.POST['email']
	password = request.POST['password']

	if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
		messages.error(request, 'Enter a valid Email')
		return redirect('login')

	if len(password) < 3:
		messages.error(request, 'Provide a Valid Password')
		return redirect('login')

	UserModel = get_user_model()


	try:
		user = UserModel.objects.get(email=username)

		if not user.is_superuser:
			messages.error(request, "You don't have the permission to Log In!")
			return redirect('login')

		if user.check_password(password):
			auth_login(request, user)
			messages.success(request, 'Login Success!')
			return redirect('dashboard')
		else:
			messages.error(request, 'Invalid Password!')
			return redirect('login')

	except UserModel.DoesNotExist:
		messages.error(request, 'Invalid Email!')
		return redirect('login')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')








