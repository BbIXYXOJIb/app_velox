# from django.shortcuts import render
from rest_framework import viewsets, mixins
from image_resizer.models import ResizeTask
from image_resizer.serializers import ResizeTaskSerializer

class ResizeTaskViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = ResizeTask.objects.all()
    serializer_class = ResizeTaskSerializer

    def create(self, request, *args, **kwargs):
        # create task
        #if successful then change status to processing in request
        return super().create(request, *args, **kwargs)