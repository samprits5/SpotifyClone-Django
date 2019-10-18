from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import get_user_model, logout


# Create your views here.


def index(request):	
	return render(request, 'adminTemplates/login/login.html')


def login(request):
	username = request.POST['email']
	password = request.POST['password']

	UserModel = get_user_model()


	try:
		user = UserModel.objects.get(email=username)

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








