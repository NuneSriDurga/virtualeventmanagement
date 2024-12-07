from django.contrib import admin
from .models import LiveStreamEvent

@admin.register(LiveStreamEvent)
class LiveStreamEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'created_by')
    list_filter = ('start_time',)
    search_fields = ('title', 'description')
