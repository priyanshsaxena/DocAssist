from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^docassist/', include('docassist.urls')),
    url(r'^admin/', admin.site.urls),
]
