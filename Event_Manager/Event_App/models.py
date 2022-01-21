from tkinter import Widget
from django.db import models

# Create your models here.
class EventReg(models.Model):
    event_name = models.CharField(max_length=30)
    description = models.TextField()
    location= models.CharField(max_length=30)
    poster_link = models.URLField(default='NULL')
    date_from= models.DateTimeField()
    date_to= models.DateTimeField()
    registration_deadline = models.DateTimeField()
    host_email= models.CharField(max_length=20)
    host_password= models.CharField(max_length=20)
    def __str__(self):
        return self.event_name