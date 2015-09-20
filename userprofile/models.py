from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserRole(models.Model):
	role = models.CharField(max_length=100,unique=True)
	# desc_chs = models.CharField(max_length=250)
	def __unicode__(self):
		return self.role

class Profile(models.Model):
	user = models.OneToOneField(User,related_name='myprofile')
	fullname = models.CharField(max_length=100)
	company = models.CharField(max_length=150)
	description = models.TextField(default=" ")
	logo = models.ImageField(upload_to='profile_images',blank=True)
	role = models.ForeignKey(UserRole)
	# address = models.CharField(max_length=150)
	def __unicode__(self):
		return self.user

