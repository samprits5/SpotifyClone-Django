from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from admin.homepage.models import Homepage
from admin.song.models import Song
import re
# Create your views here.

@login_required(login_url='login')
def index(request):
	
	if request.method == 'GET':
		
		data = Homepage.objects.all()

		return render(request, 'adminTemplates/homepage/index.html', {'data':data})



@login_required(login_url='login')
def edit(request, id):

	if request.method == 'GET':

		homepage = Homepage.objects.filter(pk=id)

		if not homepage:
			messages.error(request, 'No such records found!')
			return redirect('homepage-index')
		else:
			homepage = homepage.get()

			song = Song.objects.all()

			return render(request, 'adminTemplates/homepage/edit.html', {'homepage':homepage, 'song':song})



@login_required(login_url='login')
def update(request, id):

	if request.method == 'POST':

		name = request.POST['name']
		artist = request.POST['artist']
		song_id = request.POST['song']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?\_?\-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid Song Name')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^[(a-z)?(A-Z)?(0-9)?\_?\-?\.?\,?!?\s]+$',artist):

			messages.error(request, 'Enter a valid Artist Name')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


		song = Song.objects.filter(pk=song_id)

		if not song:
			messages.error(request, 'No such Song found!')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else:
			song = song.get()




		homepage = Homepage.objects.filter(pk=id)

		if not homepage:
			messages.error(request, 'No such records found!')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else:
			homepage = homepage.get()

			homepage.name = name
			homepage.artist = artist
			homepage.song = song

			homepage.save()

			messages.success(request, 'Record Updated!')
			
			return redirect('homepage-index')





