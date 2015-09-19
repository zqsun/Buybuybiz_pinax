from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from myaccount.models import bizCategory, bizGoal, bizProject, projectPic
from myaccount.forms import ProjectForm, projectPicform

import os
from django.conf import settings
# Create your views here.
@login_required
def index(request):
	projectsCount = bizProject.objects.filter(post_by=request.user).count()
	context = {'projectsCount': projectsCount}
	return render(request, 'myaccount/index.html', context)

@login_required
def addProject(request):
	# tflag = "add"
	# print request.user.id
	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	# added = False
	
	if request.method == 'POST':
		project_form = ProjectForm(request.POST)
		pic_form = projectPicform(request.POST)
		if project_form.is_valid() :
			project = project_form.save(commit=False)
			project.post_by = request.user
			project.save()
			# added = True
			# message = "Product: "+product.name+" is added successfullly."
			messages.success(request, 'Project: %s is successfullly added.' % project.name)

		if pic_form.is_valid():
			if 'picture' in request.FILES:
				pic = pic_form.save(commit=False)
				pic.project = project
				pic.picture = request.FILES['picture']
				pic.save()
		return HttpResponseRedirect(reverse('myaccount:myProjects'))
	else:
		project_form = ProjectForm()
		pic_form = projectPicform()

	context = {'project_form':project_form,'pic_form':pic_form}
	return render(request, 'myaccount/addproject.html', context)
	# return HttpResponse("Hello, world. You're at the Add product.")

@login_required
def editProject(request,project_id):
	tflag = "edit"
	# print request.user.id
	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	# added = False
	p = bizProject.objects.get(pk=project_id)
	try:
		pic_pre = projectPic.objects.get(project_id = p)
	except projectPic.DoesNotExist:
		pic_pre = None
	if p.post_by != request.user:
		return HttpResponse("You don't have permission")
	if request.method == 'POST':
		project_form = ProjectForm(request.POST,instance=p)
		pic_form = projectPicform(request.POST,instance=pic_pre)
		if project_form.is_valid():
			project = project_form.save(commit=False)
			project.post_by = request.user
			project.save()
			# added = True
			messages.success(request, 'Project: %s is successfullly updated.' % project.name)

		if pic_form.is_valid():
			pic_new = pic_form.save(commit=False)
			pic_new.project = project
			if 'picture' in request.FILES:
				# Delete the old picture
				if pic_pre:
					os.remove(os.path.join(settings.MEDIA_ROOT,pic_pre.picture.name))
				pic_new.picture = request.FILES['picture']
				pic_new.save()

		return HttpResponseRedirect(reverse('myaccount:myProjects'))
	else:
		project_form = ProjectForm(instance=p)
		pic_form = projectPicform(instance=pic_pre)
	context = {'project_form':project_form,'pic_form':pic_form,'tflag':tflag, 'project_id':project_id}
	return render(request, 'myaccount/addproject.html', context)
	# return HttpResponse("Hello, world. You're at the Add product.")

def delProject(request,project_id):
	project = bizProject.objects.get(pk=project_id)
	try:
		pic = projectPic.objects.get(project = project)
	except projectic.DoesNotExist:
		pic = None
	# pic = productPic.objects.get(product = product)
	if project.post_by != request.user:
		return HttpResponse("You don't have permission")
	else:
		if pic:
			os.remove(os.path.join(settings.MEDIA_ROOT,pic.picture.name))
			pic.delete()
		messages.success(request, 'Project: %s is successfullly deleted.' % project.name)
		project.delete()
		return HttpResponseRedirect(reverse('myaccount:myprojects'))

@login_required
def myProjects(request):
	projects = bizProject.objects.filter(post_by=request.user)
	# paginator = Paginator(products,5)
	# page = request.GET.get('page')
	# try:
	# 	li = paginator.page(page)
	# except PageNotAnInteger:
	# 	li = paginator.page(1)
	# except EmptyPage:
	# 	li = paginator.page(paginator.num_pages)
	# context = {'listings':li}
	context = {'listings':projects}
	return render(request, 'myaccount/myprojects.html', context)
	# return HttpResponse("Hello, world. You're at the polls index.")
