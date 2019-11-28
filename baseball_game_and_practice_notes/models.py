from django.db import models

from .consts import WEATHER_CHOICES
from .consts import NUMBER_CHOICES_1
from .consts import NUMBER_CHOICES_2
from .consts import NUMBER_CHOICES_3
from .consts import POSITION_CHOICES
from .consts import VICTORY_OR_DEFEAT_CHOICES
from .consts import FIELDER_RESULT_CHOICES


class PracticeNote(models.Model):
    date = models.DateField()
    weather = models.CharField(max_length=10, choices=WEATHER_CHOICES)
    practice_menu = models.TextField(max_length=1000)
    batting = models.TextField(max_length=1000, blank=True, null=True)
    defense = models.TextField(max_length=1000, blank=True, null=True)
    running = models.TextField(max_length=1000, blank=True, null=True)
    advice = models.TextField(max_length=1000, blank=True, null=True)
    next_goal = models.TextField(max_length=1000)


class GameNote(models.Model):
    date = models.DateField()
    weather = models.CharField(max_length=10, choices=WEATHER_CHOICES)
    opponent_team = models.CharField(max_length=50)
    victory_or_defeat = models.CharField(max_length=10,choices=VICTORY_OR_DEFEAT_CHOICES)
    morning_condition = models.IntegerField(choices=NUMBER_CHOICES_1)
    condition_before_game = models.IntegerField(choices=NUMBER_CHOICES_1)
    position_1 = models.CharField(max_length=10, choices=POSITION_CHOICES, blank=True, null=True)
    position_2 = models.CharField(max_length=10, choices=POSITION_CHOICES, blank=True, null=True)
    position_3 = models.CharField(max_length=10, choices=POSITION_CHOICES, blank=True, null=True)
    position_4 = models.CharField(max_length=10, choices=POSITION_CHOICES, blank=True, null=True)
    position_5 = models.CharField(max_length=10, choices=POSITION_CHOICES, blank=True, null=True)
    fielder_result_1 = models.CharField(max_length=10, choices=FIELDER_RESULT_CHOICES, blank=True, null=True)
    fielder_result_1_RBI = models.IntegerField(choices=NUMBER_CHOICES_3, default=0)
    fielder_result_2 = models.CharField(max_length=10, choices=FIELDER_RESULT_CHOICES, blank=True, null=True)
    fielder_result_2_RBI = models.IntegerField(choices=NUMBER_CHOICES_3, default=0)
    fielder_result_3 = models.CharField(max_length=10, choices=FIELDER_RESULT_CHOICES, blank=True, null=True)
    fielder_result_3_RBI = models.IntegerField(choices=NUMBER_CHOICES_3, default=0)
    fielder_result_4 = models.CharField(max_length=10, choices=FIELDER_RESULT_CHOICES, blank=True, null=True)
    fielder_result_4_RBI = models.IntegerField(choices=NUMBER_CHOICES_3, default=0)
    fielder_result_5 = models.CharField(max_length=10, choices=FIELDER_RESULT_CHOICES, blank=True, null=True)
    fielder_result_5_RBI = models.IntegerField(choices=NUMBER_CHOICES_3, default=0)
    fielder_result_6 = models.CharField(max_length=10, choices=FIELDER_RESULT_CHOICES, blank=True, null=True)
    fielder_result_6_RBI = models.IntegerField(choices=NUMBER_CHOICES_3, default=0)
    fielder_result_7 = models.CharField(max_length=10, choices=FIELDER_RESULT_CHOICES, blank=True, null=True)
    fielder_result_7_RBI = models.IntegerField(choices=NUMBER_CHOICES_3, default=0)
    fielder_result_8 = models.CharField(max_length=10, choices=FIELDER_RESULT_CHOICES, blank=True, null=True)
    fielder_result_8_RBI = models.IntegerField(choices=NUMBER_CHOICES_3, default=0)
    fielder_result_9 = models.CharField(max_length=10, choices=FIELDER_RESULT_CHOICES, blank=True, null=True)
    fielder_result_9_RBI = models.IntegerField(choices=NUMBER_CHOICES_3, default=0)
    fielder_result_10 = models.CharField(max_length=10, choices=FIELDER_RESULT_CHOICES, blank=True, null=True)
    fielder_result_10_RBI = models.IntegerField(choices=NUMBER_CHOICES_3, default=0)
    stealing_second_base_count = models.IntegerField(choices=NUMBER_CHOICES_2, blank=True, null=True)
    stealing_third_base_count = models.IntegerField(choices=NUMBER_CHOICES_2, blank=True, null=True)
    good_point_in_the_game = models.TextField(max_length=1000, blank=True, null=True)
    bad_point_in_the_game = models.TextField(max_length=1000, blank=True, null=True)
    advice = models.TextField(max_length=1000, blank=True, null=True)
    feelings_for_the_next_game = models.TextField(max_length=1000)
    memo = models.TextField(max_length=1000, blank=True, null=True)
