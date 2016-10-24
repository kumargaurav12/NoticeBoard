from django.db import models

# Create your models here.

class Event(models.Model):
	event_name = models.CharField(max_length = 75)
	event_description = models.CharField(max_length = 500)
	event_date = models.DateField()
	event_timings = models.TimeField()
	event_venue = models.CharField(max_length = 75)
	event_fees = models.IntegerField( default = 0)
	event_steats = models.IntegerField( default = 36)
	event_organizer_details = models.CharField(max_length= 140)

	def __str__(self):
		return self.event_name + "; " + self.event_venue + "; " + str(self.event_date)