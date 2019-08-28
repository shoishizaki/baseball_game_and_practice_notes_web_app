from django.db import models

# Create your models here.

class PracticeNote(models.Model):
    date = models.DateField()
    weather = models.CharField(max_length=10)
    practice_menu = models.TextField(max_length=1000)
    batting = models.TextField(max_length=1000)
    defense = models.TextField(max_length=1000)
    running = models.TextField(max_length=1000)
    advice = models.TextField(max_length=1000)
    next_goal = models.TextField(max_length=1000)
