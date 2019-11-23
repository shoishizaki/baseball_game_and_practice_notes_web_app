from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import PracticeNote
from .forms import PracticeNoteForm


@login_required
def index(request):
    return render(request,'baseball_game_and_practice_notes/first_page.html')


@login_required
def check_practice_note_page(request):
    practice_note_list = PracticeNote.objects.all()
    practice_note_dict = {'practice_note_list':practice_note_list}
    return render(request,'baseball_game_and_practice_notes/practice_note_checking_page.html', practice_note_dict)


@login_required
def check_practice_note_detail_page(request, pk):
    practice_note_data = PracticeNote.objects.get(pk=pk)
    practice_note_detail_dict = {'practice_note_data':practice_note_data}
    return render(request, 'baseball_game_and_practice_notes/practice_note_detail_page.html', practice_note_detail_dict)


@login_required
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

@login_required
def confirm_deletion_practice_note(request, pk):
    practice_note_data = PracticeNote.objects.get(pk=pk)
    confirm_deletion_practice_note_dict = {'practice_note_data':practice_note_data}
    return render(request, 'baseball_game_and_practice_notes/practice_note_deletion_confirmation_page.html', confirm_deletion_practice_note_dict)


@login_required
def edit_practice_note(request, pk):
    practice_note_data = get_object_or_404(PracticeNote, pk=pk)
    print(practice_note_data.date)
    print("{0:%Y-%m-%d}".format(practice_note_data.date))
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
            'practice_note_data_date': "{0:%Y-%m-%d}".format(practice_note_data.date),
            'practice_note_data_practice_menu': practice_note_data.practice_menu.strip(),
            'practice_note_data_batting': practice_note_data.batting.strip(),
            'practice_note_data_defense': practice_note_data.defense.strip(),
            'practice_note_data_running': practice_note_data.running.strip(),
            'practice_note_data_advice': practice_note_data.advice.strip(),
            'practice_note_data_next_goal': practice_note_data.next_goal.strip(),
        }
        return render(request, 'baseball_game_and_practice_notes/practice_note_edit_page.html', edit_practice_note_dict)


def sign_up_func(request):
    if request.method == 'POST':
        new_username = request.POST['username']
        new_password = request.POST['password']
        try:
            User.objects.get(username=new_username)
            return render(request, 'sign_up.html', {'error':'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(new_username, '', new_password)
            login(request, user)
            return redirect('index')
    return render(request, 'sign_up.html')


def loginfunc(request):
    if request.method == 'POST':
        authentication_username = request.POST['username']
        authentication_password = request.POST['password']
        print(authentication_username)
        print(authentication_password)
        user = authenticate(request, username=authentication_username, password=authentication_password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error':'usernameもしくはpasswordが間違っています'})
    return render(request, 'login.html')


def logoutfunc(request):
    logout(request)
    return redirect('login')
    