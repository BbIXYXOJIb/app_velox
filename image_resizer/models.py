from django.db import models
from image_resizer.types import StatusTypes

# Create your models here.

class ResizeTask(models.Model):
    status = models.CharField(choices=StatusTypes.choices, max_length=15,
                              default=StatusTypes.NOT_STARTED,
                              verbose_name='Статус обработки задачи')
    target_width = models.PositiveSmallIntegerField(verbose_name='Ширина для ресайза')
    target_height = models.PositiveSmallIntegerField(verbose_name='Высота для ресайза')
    img = models.FileField(verbose_name='Файл картинки')
