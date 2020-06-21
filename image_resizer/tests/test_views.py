from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APIRequestFactory

from image_resizer.serializers import ResizeTaskSerializer
from image_resizer.tests.utils import create_task, get_temporary_image
from image_resizer.types import StatusTypes


class ResizeTaskRetrieveTest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.factory = APIRequestFactory()

    def test_task_not_done(self):

        task = create_task(status=StatusTypes.PROCESSING)
        url = reverse('image_resizer:default:resize_task-detail', args=[task.id])
        request = self.factory.get(url)  # for serializer context
        serializer = ResizeTaskSerializer(task, context={"request": request})
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertDictEqual(resp.data, serializer.data)

    def test_task_done(self):
        task = create_task(status=StatusTypes.DONE)
        url = reverse('image_resizer:default:resize_task-detail', args=[task.id])
        request = self.factory.get(url)  # for serializer context
        serializer = ResizeTaskSerializer(task, context={"request": request})
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 303)
        self.assertDictEqual(resp.data, serializer.data)

class ResizeTaskCreateTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create(self):
        data = {'target_width': 9999, 'target_height': 9999,
                'img': get_temporary_image()}

        url = reverse('image_resizer:default:resize_task-list')
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, 202)



