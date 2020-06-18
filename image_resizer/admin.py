from django.contrib import admin
from image_resizer.models import ResizeTask
# Register your models here.

@admin.register(ResizeTask)
class ResizeTaskAdmin(admin.ModelAdmin):
    pass