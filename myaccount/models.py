from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class bizCategory(models.Model):
	category = models.CharField(max_length=250,unique=True)
	# desc_chs = models.CharField(max_length=250)
	def __unicode__(self):
		return self.category

class bizGoal(models.Model):
	goal = models.CharField(max_length=250,unique=True)
	def __unicode__(self):
		return self.goal

class bizProject(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	# quantity = models.DecimalField(max_digits=11,decimal_places=2)
	price = models.DecimalField(max_digits=11,decimal_places=2,default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	post_by = models.ForeignKey(User)
	category = models.ForeignKey(bizCategory)
	goal = models.ForeignKey(bizGoal)
	def __unicode__(self):
		return self.name

class projectPic(models.Model):
	project = models.ForeignKey(bizProject)
	picture = models.ImageField(upload_to='product_images',blank=True)