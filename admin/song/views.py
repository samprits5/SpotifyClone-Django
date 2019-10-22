from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from admin.genre.models import Genre
from admin.mood.models import Mood
from admin.artist.models import Artist
from admin.song.models import Song
import re
# Create your views here.


@login_required(login_url='login')
def add(request):

	genre = Genre.objects.all()

	mood = Mood.objects.all()

	artist = Artist.objects.all()

	return render(request, 'adminTemplates/song/add.html', {'genre':genre, 'mood':mood, 'artist':artist})


@login_required(login_url='login')
def save(request):

	if request.method == 'POST':

		name = request.POST['name']
		desc = request.POST['desc']
		length = request.POST['length']
		mood_id = request.POST['mood']
		genre_id = request.POST['genre']
		artist_id = request.POST['artist']

		songFile = request.FILES['file']

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid Song Name')
			return redirect('song-add')

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?!?\s]+$',desc):

			messages.error(request, 'Enter a valid Song Description')
			return redirect('song-add')

		if not re.match('^\d{2}:\d{2}$',length):

			messages.error(request, 'Enter a valid Song Length')
			return redirect('song-add')

		if not songFile.name.split('.')[-1] in ['mp3','wav']:

			messages.error(request, 'Invalid File Type')
			return redirect('song-add')


		genre = Genre.objects.filter(pk=genre_id)

		if not genre:
			messages.error(request, 'No such genre found!')
			return redirect('song-add')
		else:
			genre = genre.get()


		artist = Artist.objects.filter(pk=artist_id)

		if not artist:
			messages.error(request, 'No such artist found!')
			return redirect('song-add')
		else:
			artist = artist.get()


		mood = Mood.objects.filter(pk=mood_id)

		if not mood:
			messages.error(request, 'No such mood found!')
			return redirect('song-add')
		else:
			mood = mood.get()


		song = Song(song_name=name, song_des=desc, song_length=length, song_file=songFile, artist_name=artist, mood_name=mood, genre_name=genre)

		song.save()

		messages.success(request, 'Song Added Successfully!')

		return redirect('song-index')



@login_required(login_url='login')
def index(request):
	
	if request.method == 'GET':
		
		data = Song.objects.all()

		return render(request, 'adminTemplates/song/index.html', {'data':data})


@login_required(login_url='login')
def delete(request, id):

	if request.method == 'GET':

		song = Song.objects.filter(pk=id)

		if not song:
			messages.error(request, 'No such records found!')
			return redirect('song-index')
		else:
			# For Deleting The Song File From FileSystem
			song_obj = song.get()
			song_obj.song_file.delete()
			# For Deleting The Database Record
			song.delete()
			messages.success(request, 'Record Deleted!')

		return redirect('song-index')


@login_required(login_url='login')
def edit(request, id):

	if request.method == 'GET':

		song = Song.objects.filter(pk=id)

		genre = Genre.objects.all()

		mood = Mood.objects.all()

		artist = Artist.objects.all()

		if not song:
			messages.error(request, 'No such records found!')
			return redirect('song-index')
		else:
			song = song.get()

			return render(request, 'adminTemplates/song/edit.html', {'song':song, 'genre':genre, 'mood':mood, 'artist':artist})


@login_required(login_url='login')
def update(request, id):

	if request.method == 'POST':

		name = request.POST['name']
		desc = request.POST['desc']
		length = request.POST['length']
		mood_id = request.POST['mood']
		genre_id = request.POST['genre']
		artist_id = request.POST['artist']



		artist = Artist.objects.filter(pk=artist_id)

		if not artist:
			messages.error(request, 'No such Artist found!')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else:
			artist = artist.get()


		genre = Genre.objects.filter(pk=genre_id)

		if not genre:
			messages.error(request, 'No such Genre found!')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else:
			genre = genre.get()


		mood = Mood.objects.filter(pk=mood_id)

		if not mood:
			messages.error(request, 'No such Mood found!')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		else:
			mood = mood.get()



		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?\s]+$',name):

			messages.error(request, 'Enter a valid Song Name')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^[(a-z)?(A-Z)?(0-9)?_?-?\.?\,?!?\s]+$',desc):

			messages.error(request, 'Enter a valid Song Description')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if not re.match('^\d{2}:\d{2}$',length):

			messages.error(request, 'Enter a valid Song Length')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



		song = Song.objects.filter(pk=id)

		if not song:
			messages.error(request, 'No such records found!')
			return redirect('song-index')
		else:
			song = song.get()



		if 'file' in request.FILES:

			songFile = request.FILES['file']

			if not songFile.name.split('.')[-1] in ['mp3','wav']:

				messages.error(request, 'Invalid File Type')
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

			song.song_file.delete()

			song.song_name = name
			song.song_des = desc
			song.song_length = length
			song.artist_name = artist
			song.mood_name = mood
			song.genre_name = genre
			song.song_file = songFile

			song.save()

			messages.success(request, 'Record Updated!')
			
			return redirect('song-index')


		else:

			song.song_name = name
			song.song_des = desc
			song.song_length = length
			song.artist_name = artist
			song.mood_name = mood
			song.genre_name = genre

			song.save()

			messages.success(request, 'Record Updated!')
			
			return redirect('song-index')


@login_required(login_url='login')
def details(request, id):

	if request.method == 'GET':

		song = Song.objects.filter(pk=id)

		if not song:
			messages.error(request, 'No such records found!')
			return redirect('user-index')
		else:
			song = song.get()

			return render(request, 'adminTemplates/song/details.html', {'song':song})







