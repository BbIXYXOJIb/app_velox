from image_resizer.models import ResizeTask
from rest_framework import serializers
from image_resizer.types import StatusTypes

class ResizeTaskSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    status = serializers.ChoiceField(choices=StatusTypes.choices, read_only=True)
    target_width = serializers.IntegerField(write_only=True)
    target_height = serializers.IntegerField(write_only=True)
    img = serializers.ImageField()
    class Meta:
        model = ResizeTask
        fields  = ('id', 'status', 'target_width', 'target_height', 'img')

    def validate(self, attrs):
        if attrs['target_width'] > 9999 or attrs['target_height'] > 9999:
            raise serializers.ValidationError("Image width and height dimensions should <10000.")

        if attrs['target_width'] <=0 or attrs['target_height'] <= 0:
            raise serializers.ValidationError("Image dimensions can not be 0 or less.")

        return attrs

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if ret.get('status') != StatusTypes.DONE:
            del ret['img']
        return ret
