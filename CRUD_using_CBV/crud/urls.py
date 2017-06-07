from django.conf.urls import url

from .views import (
	CounterCreateView, 
	CounterUpdateView, 
	CounterDeleteView, 
	CounterDetailView, 
	CounterListView )


urlpatterns=[
url(r'^create/count/$', CounterCreateView.as_view(), name='create-count'),
url(r'^update/count/(?P<pk>\d+)$', CounterUpdateView.as_view(), name='update-count'),
url(r'^delete/count/(?P<pk>\d+)$', CounterDeleteView.as_view(), name='delete-count'),
url(r'^detail/count/(?P<pk>\d+)$', CounterDetailView.as_view(), name='detail-count'),
url(r'^list/count/$', CounterListView.as_view(), name='list-count'),

]
