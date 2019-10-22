from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from admin.user.models import CustomUser
# Create your views here.

@login_required(login_url='login')
def index(request):
	
	if request.method == 'GET':
		
		data = CustomUser.objects.all()

		return render(request, 'adminTemplates/user/index.html', {'data':data})


@login_required(login_url='login')
def details(request, id):

	if request.method == 'GET':

		usr = CustomUser.objects.filter(pk=id)

		if not usr:
			messages.error(request, 'No such records found!')
			return redirect('user-index')
		else:
			usr = usr.get()

			return render(request, 'adminTemplates/user/details.html', {'usr':usr})




