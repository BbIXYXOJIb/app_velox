# from django.shortcuts import render
import traceback

from django_q.tasks import async_task
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from image_resizer.models import ResizeTask
from image_resizer.serializers import ResizeTaskSerializer
from image_resizer.types import StatusTypes
from image_resizer.utils import resize_image


class ResizeTaskViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = ResizeTask.objects.all()
    serializer_class = ResizeTaskSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        task_status = StatusTypes.PROCESSING
        serializer = ResizeTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task_object = ResizeTask.objects.create(status=task_status,
                                                **serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        async_task(resize_image, task_object)
        return Response(data={'task_id': task_object.id}, status=status.HTTP_202_ACCEPTED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        response_status = status.HTTP_200_OK
        if instance.status == StatusTypes.DONE:
            response_status = status.HTTP_303_SEE_OTHER
        return Response(serializer.data, status=response_status)
