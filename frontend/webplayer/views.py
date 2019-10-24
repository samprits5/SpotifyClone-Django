from django.shortcuts import render
from admin.homepage.models import Homepage
from admin.song.models import Song
# Create your views here.

def index(request):
	
	data = Homepage.objects.all()

	song = Song.objects.filter(pk=2).get()

	return render(request, 'frontendTemplates/webplayer/index.html', {'data':data, 'song':song})


def index_id(request, sid):
	
	data = Homepage.objects.all()

	song = Song.objects.filter(pk=sid)

	if not song:
		song = Song.objects.filter(pk=2).get()
	else:
		song = song.get()

	return render(request, 'frontendTemplates/webplayer/index.html', {'data':data, 'song':song})