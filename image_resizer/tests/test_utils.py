
from django.test import TestCase

from image_resizer.utils import determine_ext, resize_image
from image_resizer.tests.utils import get_temporary_image, create_task


class DetermineExtTest(TestCase):

    def test_jpeg(self):
        filename = 'test.jpeg'
        ext = determine_ext(filename)
        self.assertEqual('jpeg', ext.lower())

    def test_jpg(self):
        filename = 'test.jpg'
        ext = determine_ext(filename)
        self.assertEqual('jpeg', ext.lower())

    def test_png(self):
        filename = 'test.png'
        ext = determine_ext(filename)
        self.assertEqual('png', ext.lower())



class ResizeImageTest(TestCase):

    def test_resize_img(self):
        target_width = 1920
        target_height = 1080
        task = create_task(target_width=target_width,
                           target_height=target_height)
        resize_image(task)
        self.assertSetEqual({target_width, target_height}, {task.img.width, task.img.height})