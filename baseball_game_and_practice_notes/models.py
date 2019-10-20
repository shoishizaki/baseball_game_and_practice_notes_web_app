from django.db import models

# Create your models here.

class PracticeNote(models.Model):
    date = models.DateField()
    weather = models.CharField(max_length=10)
    practice_menu = models.TextField(max_length=1000)
    batting = models.TextField(max_length=1000, blank=True, null=True)
    defense = models.TextField(max_length=1000, blank=True, null=True)
    running = models.TextField(max_length=1000, blank=True, null=True)
    advice = models.TextField(max_length=1000, blank=True, null=True)
    next_goal = models.TextField(max_length=1000)
