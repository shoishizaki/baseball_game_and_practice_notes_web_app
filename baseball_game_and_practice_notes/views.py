from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'baseball_game_and_practice_notes/first_page.html')

def check_practice_note_page(request):
    practice_note_dict = {}
    return render(request,'baseball_game_and_practice_notes/practice_note_checking_page.html')