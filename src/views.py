from django.shortcuts import render
from src.models  import Event
import datetime

# Create your views here.
def events(request):
	now = datetime.datetime.now()
	tmrw = datetime.date.today() + datetime.timedelta( days = 1)
	tmrw_day = str(tmrw.strftime("%d"))
	events_today= Event.objects.filter(event_date__day = now.strftime( "%d")) #strftime get the module
	events_tmrw = Event.objects.filter(event_date__day = tmrw_day)

	events_all = Event.objects.all()
	return render(request, 'events.html',{'x' : events_all, 'events_today' : events_today, 'events_tmrw': events_tmrw})


def event_detail(request, event_id):
	detail_event = Event.objects.get(pk = event_id)

	return render(request, 'event_detail.html', {'detail_event': detail_event })