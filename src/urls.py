from django.conf.urls import url
from src import views

urlpatterns = [
				url(r'^$',views.events, name = 'events'),
				url(r'^(?P<event_id>\d+)/$',views.event_detail, name = 'event_detail')

]


#url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),