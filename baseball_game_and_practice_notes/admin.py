from django.contrib import admin
from baseball_game_and_practice_notes.models import PracticeNote
from baseball_game_and_practice_notes.models import GameNote


admin.site.register(PracticeNote)
admin.site.register(GameNote)
