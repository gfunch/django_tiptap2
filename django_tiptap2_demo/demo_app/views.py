from .models import Note
from .forms import NoteForm
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class NoteCreateView(CreateView):
    model = Note
    fields = "__all__"

    template_name = "note_view.html"
