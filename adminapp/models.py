from django.db import models
from django.contrib.auth.models import User

class LiveStreamEvent(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    stream_url = models.URLField(help_text="Embed URL for the live stream (e.g., YouTube, Twitch)")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
