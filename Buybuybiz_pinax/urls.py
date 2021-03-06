from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin
import userprofile.views

urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^team/$", TemplateView.as_view(template_name="teampage.html"), name="team"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/signup/$", userprofile.views.SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
    url(r'^messages/', include('postman.urls')),
    url(r'^partners/', include('partners.urls')),
    url(r'^myaccount/',include('myaccount.urls', namespace="myaccount")),
    url(r'^',include('mainsite.urls', namespace="mainsite")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
