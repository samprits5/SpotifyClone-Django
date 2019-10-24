from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from admin.user.models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model, logout
from django.contrib.auth import login as auth_login
from admin.homepage.models import Homepage
import re

# Create your views here.

def index(request):
	
	data = Homepage.objects.all()

	return render(request, 'frontendTemplates/home/index.html', {'data':data})



def signup(request):
	return render(request, 'frontendTemplates/signup/index.html')


def signup_post(request):
	if request.method == 'POST':

		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		number = request.POST['number']
		gender = request.POST['gender']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid Name')
			return redirect('home-signup')

		if not re.match('^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$',email):

			messages.error(request, 'Enter a valid Email')
			return redirect('home-signup')

		if not re.match('^[\d]{10,15}$',number):

			messages.error(request, 'Enter a valid Number')
			return redirect('home-signup')


		usr = CustomUser(name=name, email=email, password=make_password(password), usr_phone=number, usr_gender=gender)

		usr.save()

		messages.success(request, 'Successfully Registered!')

		return redirect('home-signup')


def login(request):
	return render(request, 'frontendTemplates/login/index.html')


def login_post(request):
	username = request.POST['email']
	password = request.POST['password']

	if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username):
		messages.error(request, 'Enter a valid Email')
		return redirect('home-login')

	if len(password) < 3:
		messages.error(request, 'Provide a Valid Password')
		return redirect('home-login')

	UserModel = get_user_model()


	try:
		user = UserModel.objects.get(email=username)

		if user.check_password(password):
			auth_login(request, user)
			return redirect('home-index')
		else:
			messages.error(request, 'Invalid Password!')
			return redirect('home-login')

	except UserModel.DoesNotExist:
		messages.error(request, 'Invalid Email!')
		return redirect('home-login')

@login_required(login_url='home-login')
def logout_post(request):
    logout(request)
    return redirect('home-index')