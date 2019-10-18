from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from admin.genre.models import Genre
import re
# Create your views here.

@login_required(login_url='login')
def add(request):
	return render(request, 'adminTemplates/genre/add.html')

@login_required(login_url='login')
def save(request):

	if request.method == 'POST':

		name = request.POST['name']
		desc = request.POST['desc']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid Genre Name')
			return redirect('genre-add')

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?!?\s]+$',desc):

			messages.error(request, 'Enter a valid Genre Description')
			return redirect('genre-add')


		genr = Genre(genre_name=name, genre_des=desc)

		genr.save()

		messages.success(request, 'Genre Added Successfully!')

		return redirect('genre-index')

@login_required(login_url='login')
def index(request):
	
	if request.method == 'GET':
		
		data = Genre.objects.all()

		return render(request, 'adminTemplates/genre/index.html', {'data':data})


@login_required(login_url='login')
def delete(request, id):

	if request.method == 'GET':

		genr = Genre.objects.filter(pk=id)

		if not genr:
			messages.error(request, 'No such records found!')
			return redirect('genre-index')
		else:
			genr = genr.delete()
			messages.success(request, 'Record Deleted!')

		return redirect('genre-index')


@login_required(login_url='login')
def edit(request, id):

	if request.method == 'GET':

		genr = Genre.objects.filter(pk=id)

		if not genr:
			messages.error(request, 'No such records found!')
			return redirect('genre-index')
		else:
			genr = genr.get()

			return render(request, 'adminTemplates/genre/edit.html', {'genr':genr})



@login_required(login_url='login')
def update(request, id):

	if request.method == 'POST':

		name = request.POST['name']
		desc = request.POST['desc']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid Genre Name')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?!?\s]+$',desc):

			messages.error(request, 'Enter a valid Genre Description')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		genr = Genre.objects.filter(pk=id)

		if not genr:
			messages.error(request, 'No such records found!')
			return redirect('genre-index')
		else:
			genr = genr.get()

			genr.genre_name = name
			genr.genre_des = desc

			genr.save()

			messages.success(request, 'Record Updated!')
			
			return redirect('genre-index')










