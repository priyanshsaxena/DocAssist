from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index.html', views.index, name='index'),
	url(r'^disease.html', views.disease, name='disease'),
	url(r'^training.html', views.training, name='training'),
	url(r'^newdata.html', views.newdata, name='newdata'),
	url(r'^show.html', views.get_query, name='show'),
	url(r'^search.html', views.search, name='search'),
]