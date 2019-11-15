from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

from .models import PracticeNote
from .forms import PracticeNoteForm

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
        PracticeNote.objects.create(
            date = form.cleaned_data['date'],
            weather = form.cleaned_data['weather'],
            practice_menu = form.cleaned_data['practice_menu'].strip(),
            batting = form.cleaned_data['batting'].strip(),
            defense = form.cleaned_data['defense'].strip(),
            running = form.cleaned_data['running'].strip(),
            advice = form.cleaned_data['advice'].strip(),
            next_goal = form.cleaned_data['next_goal'].strip(),
        )
        return redirect('index')
    return render(request, 'baseball_game_and_practice_notes/practice_note_add_page.html', add_practice_note_dict)


@require_POST
def delete_practice_note(request, pk):
    practice_note_data = PracticeNote.objects.get(pk=pk)
    practice_note_data.delete()
    return redirect('check_practice_note_page')


def confirm_deletion_practice_note(request, pk):
    practice_note_data = PracticeNote.objects.get(pk=pk)
    confirm_deletion_practice_note_dict = {'practice_note_data':practice_note_data}
    return render(request, 'baseball_game_and_practice_notes/practice_note_deletion_confirmation_page.html', confirm_deletion_practice_note_dict)


def edit_practice_note(request, pk):
    practice_note_data = get_object_or_404(PracticeNote, pk=pk)
    if request.method == "POST":
        practice_note_data.date = request.POST['date'].strip()
        practice_note_data.weather = request.POST['weather'].strip()
        practice_note_data.practice_menu = request.POST['practice_menu'].strip()
        practice_note_data.batting = request.POST['batting'].strip()
        practice_note_data.defense = request.POST['defense'].strip()
        practice_note_data.running = request.POST['running'].strip()
        practice_note_data.advice = request.POST['advice'].strip()
        practice_note_data.next_goal = request.POST['next_goal'].strip()
        practice_note_data.save()
        return redirect('index')
    else:
        edit_practice_note_dict = {
            'practice_note_data': practice_note_data,
            'practice_note_data_practice_menu': practice_note_data.practice_menu.strip(),
            'practice_note_data_batting': practice_note_data.batting.strip(),
            'practice_note_data_defense': practice_note_data.defense.strip(),
            'practice_note_data_running': practice_note_data.running.strip(),
            'practice_note_data_advice': practice_note_data.advice.strip(),
            'practice_note_data_next_goal': practice_note_data.next_goal.strip(),
        }
        return render(request, 'baseball_game_and_practice_notes/practice_note_edit_page.html', edit_practice_note_dict)
