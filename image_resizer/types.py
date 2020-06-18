from django.db import models

class StatusTypes(models.TextChoices):
    NOT_STARTED = 'not_started', 'never started'
    PROCESSING = 'processing', 'processing'
    DONE = 'done', 'done'
