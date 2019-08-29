from django.shortcuts import HttpResponse
from django.shortcuts import render

from .models import PracticeNote

# Create your views here.


def index(request):
    return render(request,'baseball_game_and_practice_notes/first_page.html')


def check_practice_note_page(request):
    practice_note_list = PracticeNote.objects.all()
    practice_note_dict = {'practice_note_list':practice_note_list}
    return render(request,'baseball_game_and_practice_notes/practice_note_checking_page.html', practice_note_dict)