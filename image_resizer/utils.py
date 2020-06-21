from PIL import Image
from typing import Any
from io import BytesIO
import os
from django.core.files.base import ContentFile

from image_resizer.types import StatusTypes

def resize_image(task_object):
    width = task_object.target_width
    height = task_object.target_height
    task_object.img.open()
    resized_img = Image.open(task_object.img).\
        resize((width, height))
    resized_img_io = BytesIO()
    img_ext = determine_ext(task_object.img.name)
    resized_img.save(resized_img_io, format=img_ext)
    task_object.img.save(task_object.img.name, ContentFile(resized_img_io.getvalue()))
    task_object.status = StatusTypes.DONE
    task_object.save()
    resized_img_io.close()

def determine_ext(filename: str):
    _, ext = os.path.splitext(filename)
    ext = 'JPEG' if 'jpg' in ext.lower() else ext
    return ext.lstrip('.')