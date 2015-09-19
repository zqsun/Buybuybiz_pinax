from django.forms import ModelForm
from myaccount.models import bizProject,projectPic

class ProjectForm(ModelForm):
	class Meta:
		model = bizProject
		fields = ['name','description','price','category','goal']

class projectPicform(ModelForm):
	class Meta:
		model = projectPic
		fields = ['picture']
			
		