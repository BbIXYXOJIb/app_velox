import io

from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from rest_framework.serializers import ValidationError

from image_resizer.models import ResizeTask
# from django.test import override_settings
from image_resizer.serializers import ResizeTaskSerializer
from image_resizer.types import StatusTypes
from image_resizer.tests.utils import get_temporary_image, create_task


class ResizeTaskSerializerTest(TestCase):

    def test_width_less_than_1_validation(self):
        test_img = get_temporary_image()
        unvalidated_data = {
            'target_width': 0,
            'target_height': 256,
            'img': test_img
        }
        serializer = ResizeTaskSerializer(data=unvalidated_data)
        self.assertRaises(ValidationError, serializer.is_valid, raise_exception=True)

    def test_width_greater_than_9999_validation(self):
        test_img = get_temporary_image()
        unvalidated_data = {
            'target_width': 10000,
            'target_height': 256,
            'img': test_img
        }
        serializer = ResizeTaskSerializer(data=unvalidated_data)
        self.assertRaises(ValidationError, serializer.is_valid, raise_exception=True)

    def test_height_less_than_1_validation(self):
        test_img = get_temporary_image()
        unvalidated_data = {
            'target_width': 256,
            'target_height': 0,
            'img': test_img
        }
        serializer = ResizeTaskSerializer(data=unvalidated_data)
        self.assertRaises(ValidationError, serializer.is_valid, raise_exception=True)

    def test_height_greater_than_9999_validaton(self):
        test_img = get_temporary_image()
        unvalidated_data = {
            'target_width': 256,
            'target_height': 10000,
            'img': test_img
        }
        serializer = ResizeTaskSerializer(data=unvalidated_data)
        self.assertRaises(ValidationError, serializer.is_valid, raise_exception=True)

    def test_validation(self):
        test_img = get_temporary_image()
        unvalidated_data = {
            'target_width': 256,
            'target_height': 256,
            'img': test_img
        }
        serializer = ResizeTaskSerializer(data=unvalidated_data)
        serializer.is_valid(raise_exception=True)
        self.assertDictEqual(unvalidated_data, serializer.validated_data)

    def test_representation_status_not_done(self):
        test_img = get_temporary_image()
        data = {'status': StatusTypes.PROCESSING, 'target_width': 256, 'target_height': 256, 'img': test_img}
        task = create_task(**data)
        serializer = ResizeTaskSerializer(task)
        expected_keys = {'id', 'status'}
        actual_keys = set(serializer.data.keys())
        self.assertSetEqual(expected_keys, actual_keys)

    def test_representation_status_done(self):
        test_img = get_temporary_image()
        data = {'status': StatusTypes.DONE, 'target_width': 256, 'target_height': 256, 'img': test_img}
        task = create_task(**data)
        serializer = ResizeTaskSerializer(task)
        expected_keys = {'id', 'status', 'img'}
        actual_keys = set(serializer.data.keys())
        self.assertSetEqual(expected_keys, actual_keys)
