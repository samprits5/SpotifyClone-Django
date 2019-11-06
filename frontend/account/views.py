from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from admin.user.models import CustomUser
import re
import json
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

@login_required(login_url='home-login')
def edit_pass(request):
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()
	return render(request, 'frontendTemplates/account/edit-pass.html', {'usr':usr})


@login_required(login_url='home-login')
def update_pass(request):
	
	if request.method == 'POST':

		cpass = request.POST['cur-pass']
		npass = request.POST['new-pass']
		conpass = request.POST['con-pass']

		if (len(cpass) < 3) or (len(npass) < 3) or (len(conpass) < 3):
			messages.error(request, 'Password Length should be more than 3 characters!')
			return redirect('account-edit-pass')

		UserModel = get_user_model()

		try:
			user = UserModel.objects.get(pk=request.user.id)

			if user.check_password(cpass):

				if npass != conpass:
					messages.error(request, 'New Password does not match with Confirm Password!')
					return redirect('account-edit-pass')

				user.password = make_password(npass)
				user.save()

				auth_login(request, user)

				messages.success(request, 'Password Changed Successfully!')
				return redirect('account-index')

			else:
				messages.error(request, 'Current Password does not match!')
				return redirect('account-edit-pass')

		except UserModel.DoesNotExist:
			messages.error(request, 'Log In First!')
			return redirect('home-login')


@login_required(login_url='home-login')
def privacy(request):
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()
	return render(request, 'frontendTemplates/account/privacy.html', {'usr':usr})

@login_required(login_url='home-login')
def subs(request):
	usr = CustomUser.objects.filter(pk=request.user.id)

	if not usr:
		messages.error(request, 'Log In First!')
		return redirect('home-login')
	else:
		usr = usr.get()
	return render(request, 'frontendTemplates/account/subscription.html', {'usr':usr})

@login_required(login_url='home-login')
def profile_pic(request):
	if request.is_ajax():
		if 'file' in request.FILES.keys():

			if not request.FILES['file'].name.split('.')[-1] in ['jpg','png','jpeg']:

				return HttpResponse(json.dumps({'key':'0', 'msg':'Invalid File Type!'}))

			usr = CustomUser.objects.filter(pk=request.user.id)

			if not usr:
				messages.error(request, 'Log In First!')
				return redirect('home-login')
			else:
				usr = usr.get()

			if "team.jpg" in str(usr.profile_pic):

				usr.profile_pic = request.FILES['file']

				usr.save()

			else:
				usr.profile_pic.delete()

				usr.profile_pic = request.FILES['file']

				usr.save()


			return HttpResponse(json.dumps({'key':'1', 'msg':'Success!'}))
			
		else:
			return HttpResponse(json.dumps({'key':'0', 'msg':'No File Selected!'}))

