from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add/$',views.addProject, name='addProject'),
	url(r'^myprojects/$',views.myProjects, name='myProjects'),
	url(r'^edit/(?P<project_id>[0-9]+)/$',views.editProject, name='editProject'),
	url(r'^delete/(?P<project_id>[0-9]+)/$',views.delProject, name='delProject'),
	# url(r'^(?P<question_id>[0-9]+)/$',views.details,name='details'),
	# url(r'^login/$', auth_views.login,  {'template_name': 'account/registration/login.html'},name='login'),
	# url('', include('django.contrib.auth.urls')),
	# url(r'^transit$', views.transit, name='transit'),
	# url(r'^(?P<kw>[\w|\W]+)/(?P<cat>[\w|\W]+)/listing$', views.listing, name='listing'),
	# url(r'^(?P<cat>[\w|\W]+)/(?P<kw>[\w|\W]+)/listing$', views.listing, name='listing'),

]