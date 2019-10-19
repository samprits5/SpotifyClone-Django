from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from admin.artist.models import Artist
import re
# Create your views here.

@login_required(login_url='login')
def add(request):
	return render(request, 'adminTemplates/artist/add.html')


@login_required(login_url='login')
def save(request):

	if request.method == 'POST':

		name = request.POST['name']
		desc = request.POST['desc']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid Artist Name')
			return redirect('artist-add')

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?!?\s]+$',desc):

			messages.error(request, 'Enter a valid Artist Description')
			return redirect('artist-add')


		artist = Artist(artist_name=name, artist_des=desc)

		artist.save()

		messages.success(request, 'Artist Added Successfully!')

		return redirect('artist-index')



@login_required(login_url='login')
def index(request):
	
	if request.method == 'GET':
		
		data = Artist.objects.all()

		return render(request, 'adminTemplates/artist/index.html', {'data':data})


@login_required(login_url='login')
def delete(request, id):

	if request.method == 'GET':

		artist = Artist.objects.filter(pk=id)

		if not artist:
			messages.error(request, 'No such records found!')
			return redirect('artist-index')
		else:
			artist = artist.delete()
			messages.success(request, 'Record Deleted!')

		return redirect('artist-index')



@login_required(login_url='login')
def edit(request, id):

	if request.method == 'GET':

		artist = Artist.objects.filter(pk=id)

		if not artist:
			messages.error(request, 'No such records found!')
			return redirect('artist-index')
		else:
			artist = artist.get()

			return render(request, 'adminTemplates/artist/edit.html', {'artist':artist})



@login_required(login_url='login')
def update(request, id):

	if request.method == 'POST':

		name = request.POST['name']
		desc = request.POST['desc']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid Artist Name')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?!?\s]+$',desc):

			messages.error(request, 'Enter a valid Artist Description')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		artist = Artist.objects.filter(pk=id)

		if not artist:
			messages.error(request, 'No such records found!')
			return redirect('artist-index')
		else:
			artist = artist.get()

			artist.artist_name = name
			artist.artist_des = desc

			artist.save()

			messages.success(request, 'Record Updated!')
			
			return redirect('artist-index')























