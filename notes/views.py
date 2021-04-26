from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    noteItem = Note.objects.all()

    form = NoteForm

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    

    context = {'noteItem': noteItem, 'form': form}

    return render(request, 'notes/note_list.html', context)

def editNote(request, pk):
    noteItem = Note.objects.get(id=pk)

    form = NoteForm(instance=noteItem)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=noteItem)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'notes/edit_note.html', context)

def deleteNote(request, pk):
    noteItem = Note.objects.get(id=pk)

    if request.method == 'POST':
        noteItem.delete()
        return redirect('/')

    context = {'noteItem': noteItem}
    return render(request, 'notes/delete.html', context)               
