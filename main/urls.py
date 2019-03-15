from django.conf.urls import url
from django.contrib import admin

from .views import home_page, about_page, contact_page, login_page, register_page

urlpatterns = [
	url(r'^$', home_page),
	url(r'^about/$', about_page),
	url(r'^contact/$', contact_page),
	url(r'^admin/', admin.site.urls),
	url(r'^login/$', login_page), 
	url(r'^register/$', register_page),
]