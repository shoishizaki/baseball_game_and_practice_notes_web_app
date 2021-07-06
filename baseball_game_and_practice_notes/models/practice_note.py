from django.db import models

class PracticeNote(models.Model):
    WEATHER_CHOICES = (
        ('晴','☀️ 晴'),
        ('曇','☁️ 曇'),
        ('雨','☔️ 雨'),
        ('雪','❄️ 雪'),
    )
    date = models.DateField()
    weather = models.CharField(max_length=10)
    practice_menu = models.TextField(max_length=1000)
    batting = models.TextField(max_length=1000, blank=True, null=True)
    defense = models.TextField(max_length=1000, blank=True, null=True)
    running = models.TextField(max_length=1000, blank=True, null=True)
    advice = models.TextField(max_length=1000, blank=True, null=True)
    next_goal = models.TextField(max_length=1000)

    class Meta:
        app_label = 'baseball_game_and_practice_notes.apps'