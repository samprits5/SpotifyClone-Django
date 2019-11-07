from django.shortcuts import render, redirect
from django.http import HttpResponse
from admin.homepage.models import Homepage
from admin.song.models import Song
import random
# Create your views here.

def find_song(song_id):

	song = Song.objects.filter(pk=song_id)

	if not song:
		return False
	else:
		song = song.get()

	song_ids = Song.objects.values_list('id', flat=True)

	sid_index = list(song_ids).index(song_id)

	if sid_index == 0:

		prev_id = '-1'
		next_id = str(song_ids[sid_index+1])

	elif sid_index == len(song_ids) - 1:

		prev_id = str(song_ids[sid_index-1])
		next_id = '-1'

	else:
		prev_id = str(song_ids[sid_index-1])
		next_id = str(song_ids[sid_index+1])

	return song, prev_id, next_id

def random_song_id():
	song_ids = Song.objects.values_list('id', flat=True)

	return random.choice(list(song_ids))

def index(request):
	return redirect('player-index-id', sid=random_song_id())


def index_id(request, sid):
	
	data = Homepage.objects.all()

	if find_song(sid):
		song, prev_id, next_id = find_song(sid)
	else:
		return redirect('player-index-id', sid=random_song_id())

	return render(request, 'frontendTemplates/webplayer/index.html', {'data':data, 'song':song, 'pid': prev_id, 'nid':next_id})