from django.shortcuts import render, redirect
from django.contrib import messages
from admin.user.models import CustomUser
from django.contrib.auth.hashers import make_password
import re

# Create your views here.

def index(request):
	return render(request, 'frontendTemplates/home/index.html')



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






