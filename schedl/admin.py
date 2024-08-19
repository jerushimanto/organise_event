from django.contrib import admin
from .models import User, Event, Participant

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'email')
    search_fields = ('name', 'email')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'name', 'event_date', 'event_time', 'host')
    list_filter = ('event_date', 'host')
    search_fields = ('name', 'details', 'host__name')

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('event', 'email_id')
    search_fields = ('event__name', 'email_id')

