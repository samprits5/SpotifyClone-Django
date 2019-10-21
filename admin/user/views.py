from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from admin.user.models import CustomUser
# Create your views here.

@login_required(login_url='login')
def index(request):
	
	if request.method == 'GET':
		
		data = CustomUser.objects.all()

		return render(request, 'adminTemplates/user/index.html', {'data':data})