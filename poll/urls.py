from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^detail/(?P<Item_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^style$', views.style, name='style'),
	url(r'^addItem$', views.addItem, name='addItem'),
	url(r'^addItem/add$', views.add, name='add'),
]
