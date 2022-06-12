from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

from django_tiptap2.fields import TipTapTextField


# Create your models here.
class Note(models.Model):
    content = TipTapTextField()
    somethingMore = TipTapTextField(null=True)

    def get_absolute_url(self):
        return reverse("note-add")
