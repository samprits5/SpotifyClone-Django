from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from admin.user.models import CustomUser
import re
# Create your views here.



@login_required(login_url='home-login')
def index(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()

	return render(request, 'frontendTemplates/account/index.html', {'usr':usr})


@login_required(login_url='home-login')
def edit(request):
	
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()

	return render(request, 'frontendTemplates/account/edit.html', {'usr':usr})


@login_required(login_url='home-login')
def update(request):

	if request.method == 'POST':

		name = request.POST['name']
		email = request.POST['email']
		gender = request.POST['gender']
		mobile = request.POST['mobile']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid Name')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^[(a-z)?(A-Z)?\s?]+$',gender):

			messages.error(request, 'Enter a valid Gender')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$',email):

			messages.error(request, 'Enter a valid Email')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^[\d]{10,15}$',mobile):

			messages.error(request, 'Enter a valid Number')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		usr = CustomUser.objects.filter(pk=request.user.id)

		if not usr:
			messages.error(request, 'Log In First!')
			return redirect('home-login')
		else:
			usr = usr.get()

			usr.name = name
			usr.email = email
			usr.usr_gender = gender
			usr.usr_phone = mobile

			usr.save()

			messages.success(request, 'Profile Updated!')
			
			return redirect('account-index')












