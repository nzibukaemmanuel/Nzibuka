from django.contrib import admin
from event_management.models import Event,Speaker,Participant,Schedule,Payment
# Register your models here.
admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Participant)
admin.site.register(Schedule)
admin.site.register(Payment)
