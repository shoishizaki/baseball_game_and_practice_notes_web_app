from django.shortcuts import render
from django.shortcuts import redirect

from .models import PracticeNote
from .forms import PracticeNoteForm

# Create your views here.


def index(request):
    return render(request,'baseball_game_and_practice_notes/first_page.html')


def check_practice_note_page(request):
    practice_note_list = PracticeNote.objects.all()
    practice_note_dict = {'practice_note_list':practice_note_list}
    return render(request,'baseball_game_and_practice_notes/practice_note_checking_page.html', practice_note_dict)


def check_practice_note_detail_page(request, pk):
    practice_note_data = PracticeNote.objects.get(pk=pk)
    practice_note_detail_dict = {'practice_note_data':practice_note_data}
    return render(request, 'baseball_game_and_practice_notes/practice_note_detail_page.html', practice_note_detail_dict)


def add_practice_note(request):
    form = PracticeNoteForm(request.POST or None)
    practice_note_list = PracticeNote.objects.all()
    add_practice_note_dict = {'practice_note_list':practice_note_list, 'form':form}
    if form.is_valid():
        practice_note = PracticeNote()
        practice_note.date = form.cleaned_data['date']
        practice_note.weather = form.cleaned_data['weather']
        practice_note.practice_menu = form.cleaned_data['practice_menu']
        practice_note.batting = form.cleaned_data['batting']
        practice_note.defense = form.cleaned_data['defense']
        practice_note.running = form.cleaned_data['running']
        practice_note.advice = form.cleaned_data['advice']
        practice_note.next_goal = form.cleaned_data['next_goal']

        PracticeNote.objects.create(
            date=practice_note.date,
            weather=practice_note.weather,
            practice_menu=practice_note.practice_menu,
            batting=practice_note.batting,
            defense=practice_note.defense,
            running=practice_note.running,
            advice=practice_note.advice,
            next_goal=practice_note.next_goal,
        )
        return redirect('index')
    return render(request, 'baseball_game_and_practice_notes/practice_note_add_page.html', add_practice_note_dict)
