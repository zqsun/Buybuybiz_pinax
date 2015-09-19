from django.db import models

# Create your models here.
class Partners(models.Model):
	name = models.CharField(max_length=50)
	company = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	description = models.TextField(default=" ")
	picture = models.ImageField(upload_to='partner_images',blank=True)
	def __unicode__(self):
		return self.name