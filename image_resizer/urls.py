from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from image_resizer.views import ResizeTaskViewSet

app_name = 'image_resizer'

router = DefaultRouter()
router.register(r'resize-task', ResizeTaskViewSet)

urlpatterns = [
    url(r'^', include((router.urls, app_name), namespace='default'))
]