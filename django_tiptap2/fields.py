import uuid

from django.db import models
from django.forms import fields

from .widgets import TipTapWidget


class TipTapTextFormField(fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update({"widget": TipTapWidget()})
        super().__init__(*args, **kwargs)


class TipTapTextField(models.TextField):
    def formfield(self, **kwargs):
        return super().formfield(form_class=TipTapTextFormField, **kwargs)


class TipTapWithCommentsTextFormField(TipTapTextFormField):
    def __init__(self, *args, **kwargs):
        kwargs.update({"widget": TipTapWidget()})
        super().__init__(*args, **kwargs)

class TipTapWithCommentsTextField(TipTapTextFormField):
    def formfield(self, **kwargs):
        return super().formfield(form_class=TipTapTextFormField, **kwargs)


class TipTapFieldComment(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    author = models.CharField(max_length=255)
    created_on = models.DateTimeField(
        auto_now_add=True, editable=False,
    )
    updated_on = models.DateTimeField(
        auto_now=True, editable=False, 
    )
    node,
            jsonComments,
            from: pos,
            to: pos + (node.text?.length || 0),
            text: node.text,
    field_location = models.CharField()