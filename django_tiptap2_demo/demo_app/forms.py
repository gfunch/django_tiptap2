from django import forms
from django.contrib import admin

from .models import Note

from django_tiptap2.fields import TipTapTextFormField, TipTapTextField
from django_tiptap2.widgets import TipTapWidget


class NoteAdminForm(forms.ModelForm):
    content = forms.CharField(widget=TipTapWidget())

    class Meta:
        model = Note
        fields = "__all__"


class NoteAdmin(admin.ModelAdmin):
    form = NoteAdminForm


class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=TipTapWidget())

    class Meta:
        model = Note
        fields = "__all__"
