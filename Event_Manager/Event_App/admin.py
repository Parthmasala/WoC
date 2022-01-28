from django.contrib import admin
from Event_App.models import EventReg,ParticipantReg,ContactReg
# Register your models here.
admin.site.register(EventReg)
admin.site.register(ParticipantReg)
admin.site.register(ContactReg)