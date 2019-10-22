from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_practice_note/', views.check_practice_note_page, name='check_practice_note_page'),
    path('detail_practice_note/<int:pk>/', views.check_practice_note_detail_page, name='check_practice_note_detail_page')
]