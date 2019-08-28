from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'baseball_game_and_practice_notes/first_page.html')