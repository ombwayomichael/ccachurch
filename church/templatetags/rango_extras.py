from django import template
from church.models import Event,Social,New
import datetime

register =template.Library()
@register.inclusion_tag('church/events.html')

def get_event_list(event=None):
	now=datetime.datetime.now()
	return {'events': Event.objects.filter(eventDate__gte=now.date())[:2],'socials':Social.objects.all()[:1],'news':New.objects.all()[:2] ,'act_event': event}
