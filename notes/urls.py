from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="note_list"),
    path('edit_note/<str:pk>', views.editNote, name="edit_note"),
    path('delete/<str:pk>', views.deleteNote, name="delete"),
]