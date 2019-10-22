from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from admin.favorite.models import Favorite
# Create your views here.

@login_required(login_url='login')
def index(request):
	
	if request.method == 'GET':
		
		data = Favorite.objects.all()

		return render(request, 'adminTemplates/favorite/index.html', {'data':data})


@login_required(login_url='login')
def details(request, id):

	if request.method == 'GET':

		favorite = Favorite.objects.filter(user=id)

		if not favorite:
			messages.error(request, 'No such records found!')
			return redirect('favorite-index')
		else:
			favorite = favorite.all()

			return render(request, 'adminTemplates/favorite/details.html', {'favorite':favorite})