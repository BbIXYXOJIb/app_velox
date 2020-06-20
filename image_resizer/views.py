# from django.shortcuts import render
import traceback
from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from image_resizer.models import ResizeTask
from image_resizer.serializers import ResizeTaskSerializer
from image_resizer.utils import resize_image
from image_resizer.types import StatusTypes

from django_q.tasks import async_task

class ResizeTaskViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = ResizeTask.objects.all()
    serializer_class = ResizeTaskSerializer

    def create(self, request, *args, **kwargs):
        task_status = StatusTypes.PROCESSING
        serializer = ResizeTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task_object = ResizeTask.objects.create(status=task_status,
                                  **serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        try:
            async_task(resize_image, request.data['img'],
                       int(request.data['target_width']),
                       int(request.data['target_height']), task_object
                       )
        except Exception:
            traceback.print_exc()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED, headers=headers)