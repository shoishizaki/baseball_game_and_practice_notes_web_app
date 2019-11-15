from django import forms

WEATHER_CHOICES = (
        ('晴','晴'),
        ('曇','曇'),
        ('雨','雨'),
        ('雪','雪'),
)

class PracticeNoteForm(forms.Form):
    date = forms.DateTimeField(
        label='date',
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
        input_formats=['%Y-%m-%d']
    )

    weather = forms.ChoiceField(
        label='weather',
        widget=forms.Select,
        choices=WEATHER_CHOICES,
        required=True,
    )

    practice_menu = forms.CharField(
        label='practice_menu',
        max_length=10000,
        required=True,
        widget=forms.Textarea(),
    )

    batting = forms.CharField(
        label='batting',
        max_length=10000,
        required=False,
        widget=forms.Textarea(),
    )

    defense = forms.CharField(
        label='defense',
        max_length=10000,
        required=False,
        widget=forms.Textarea(),
    )

    running = forms.CharField(
        label='running',
        max_length=10000,
        required=False,
        widget=forms.Textarea(),
    )

    advice = forms.CharField(
        label='advice',
        max_length=10000,
        required=False,
        widget=forms.Textarea(),
    )

    next_goal = forms.CharField(
        label='next_goal',
        max_length=10000,
        required=True,
        widget=forms.Textarea(),
    )
