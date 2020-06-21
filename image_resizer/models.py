from django.db import models
from image_resizer.types import StatusTypes
import uuid

# Create your models here.

class ResizeTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(choices=StatusTypes.choices, max_length=15,
                              default=StatusTypes.NOT_STARTED,
                              verbose_name='Статус обработки задачи')
    target_width = models.PositiveSmallIntegerField(verbose_name='Ширина для ресайза')
    target_height = models.PositiveSmallIntegerField(verbose_name='Высота для ресайза')
    img = models.ImageField(verbose_name='Файл картинки')
