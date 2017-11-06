from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from rest_framework.fields import FileField

from fileupload.models import Attachment


class FileSerializer(serializers.ModelSerializer):
    """
    This serializer allows uploading a file in the ai-django-fileupload pattern

    Use like this (example for a ModelViewSet:

    @detail_route(methods=['post'], parser_classes=(MultiPartParser,))
    def attach(self, request, pk=None):
        order = self.get_object()
        serializer = self.get_serializer(order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': _('Die Datei wurde erfolgreich hochgeladen.')})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    """
    file = FileField(max_length=10 * 1024, allow_empty_file=False, help_text='The file with a size of up to 10 MB')

    class Meta:
        model = Attachment
        fields = ('file',)

    def validate(self, validated_data):
        validated_data['content_type'] = ContentType.objects.get_for_model(self.instance)
        validated_data['object_id'] = self.instance.pk
        return validated_data

    def update(self, instance, validated_data):
        return Attachment.objects.create(**validated_data)
