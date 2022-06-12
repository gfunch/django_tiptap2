import uuid
from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    object_id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    author = models.CharField(max_length=255)
    timestamp = models.DateTimeField(
        auto_now_add=True, editable=False,
    )
    text = models.TextField()
    node = models.CharField(max_length=255)
    loc_from = models.PositiveIntegerField()
    loc_to = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]