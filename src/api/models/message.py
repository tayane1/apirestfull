from django.db import models
from api.models.sujet import Sujet
from base.models.helpers.date_time_model import DateTimeModel

# Create your models here.

class Message(DateTimeModel):
    sujet = models.ForeignKey(Sujet, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()

    def __str__(self):
        return f"Message in {self.sujet.title}"
