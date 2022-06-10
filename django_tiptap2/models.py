class TipTapFieldComment(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    username = models.CharField(max_length=255)
    created_on = models.DateTimeField(
        auto_now_add=True, editable=False,
    )
    updated_on = models.DateTimeField(
        auto_now=True, editable=False, 
    )
    text = models.TextField()
    node = models.CharField(max_length=255)
    loc_from = models.PositiveIntegerField()
    loc_to = models.PositiveIntegerField()