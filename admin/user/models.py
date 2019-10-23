from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

	name = models.CharField(max_length=20, default='UserName')

	email = models.EmailField(max_length=254, unique=True)

	username = None

	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = []

	usr_phone = models.CharField(max_length=20)

	usr_gender = models.CharField(max_length=10)

	profile_pic = models.FileField(upload_to='profile/', default='profile/team.jpg')