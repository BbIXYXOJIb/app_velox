import io

from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from image_resizer.models import ResizeTask
from image_resizer.types import StatusTypes


def get_temporary_image(file_ext='png', size=(1,1)):
    fp = io.BytesIO()
    Image.new('P', size).save(fp, file_ext)
    fp.seek(0)
    temp_img = SimpleUploadedFile(name='temp.'+file_ext, content=fp.read())
    return temp_img


def create_task(status=StatusTypes.NOT_STARTED, target_width=256, target_height=256, img=None):
    test_image = get_temporary_image()
    task = ResizeTask.objects.create(status=status,
                                     target_width=target_width,
                                     target_height=target_height,
                                     img=test_image if not img else img)

    return task