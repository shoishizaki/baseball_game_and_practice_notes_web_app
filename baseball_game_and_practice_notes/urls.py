from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check_practice_note/', views.check_practice_note_page, name='check_practice_note_page'),
    path('detail_practice_note/<int:pk>/', views.check_practice_note_detail_page, name='check_practice_note_detail_page'),
    path('add_practice_note/', views.add_practice_note, name='add_practice_note_page'),
    path('delete_practice_note/<int:pk>/', views.delete_practice_note, name='delete_function_of_practice_note'),
    path('confirm_deletion_practice_note/<int:pk>', views.confirm_deletion_practice_note, name='confirm_deletion_practice_note_page'),
]