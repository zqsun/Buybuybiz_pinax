from django.conf.urls import include,url
# from . import views
from . import views

urlpatterns = [
	# url(r'^search/', include('haystack.urls',namespace="mysearch")),
	url(r'^$', views.BrowsePartners, name="browsepartners"),
]