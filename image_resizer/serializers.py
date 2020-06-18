from image_resizer.models import ResizeTask
from rest_framework import serializers
from image_resizer.types import StatusTypes

class ResizeTaskSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=StatusTypes.choices, read_only=True)
    target_width = serializers.IntegerField()
    target_height = serializers.IntegerField()
    img = serializers.FileField()
    class Meta:
        model = ResizeTask
        fields  = ('status', 'target_width', 'target_height', 'img')

    def validate(self, attrs):
        if attrs['target_width'] > 9999 or attrs['target_height'] > 9999:
            raise serializers.ValidationError("Image width and height dimensions should <10000.")

        if attrs['target_width'] <=0 or attrs['target_height'] <= 0:
            raise serializers.ValidationError("Image dimensions can not be 0 or less.")

        return attrs