from django.conf.urls import include,url
# from . import views
from . import views

urlpatterns = [
	# url(r'^search/', include('haystack.urls',namespace="mysearch")),
	url(r'^search/?$', views.my_basic_search, name="mysearch"),
	url(r'^view/(?P<project_id>[0-9]+)/$',views.viewProject, name='viewProject'),
	url(r'^browse/(?P<category_name>[\w|\W]+)/$',views.browseProject, name='browseProject'),
]