from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from admin.mood.models import Mood
import re
# Create your views here.

@login_required(login_url='login')
def add(request):
	return render(request, 'adminTemplates/mood/add.html')


@login_required(login_url='login')
def save(request):

	if request.method == 'POST':

		name = request.POST['name']
		desc = request.POST['desc']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid Mood Name')
			return redirect('mood-add')

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?!?\s]+$',desc):

			messages.error(request, 'Enter a valid Mood Description')
			return redirect('mood-add')


		mood = Mood(mood_name=name, mood_des=desc)

		mood.save()

		messages.success(request, 'Mood Added Successfully!')

		return redirect('mood-index')


@login_required(login_url='login')
def index(request):
	
	if request.method == 'GET':
		
		data = Mood.objects.all()

		return render(request, 'adminTemplates/mood/index.html', {'data':data})


@login_required(login_url='login')
def delete(request, id):

	if request.method == 'GET':

		mood = Mood.objects.filter(pk=id)

		if not mood:
			messages.error(request, 'No such records found!')
			return redirect('mood-index')
		else:
			mood = mood.delete()
			messages.success(request, 'Record Deleted!')

		return redirect('mood-index')


@login_required(login_url='login')
def edit(request, id):

	if request.method == 'GET':

		mood = Mood.objects.filter(pk=id)

		if not mood:
			messages.error(request, 'No such records found!')
			return redirect('mood-index')
		else:
			mood = mood.get()

			return render(request, 'adminTemplates/mood/edit.html', {'mood':mood})



@login_required(login_url='login')
def update(request, id):

	if request.method == 'POST':

		name = request.POST['name']
		desc = request.POST['desc']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid Mood Name')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?!?\s]+$',desc):

			messages.error(request, 'Enter a valid Mood Description')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		mood = Mood.objects.filter(pk=id)

		if not mood:
			messages.error(request, 'No such records found!')
			return redirect('mood-index')
		else:
			mood = mood.get()

			mood.mood_name = name
			mood.mood_des = desc

			mood.save()

			messages.success(request, 'Record Updated!')
			
			return redirect('mood-index')





























