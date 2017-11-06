# encoding: utf-8
from django import template
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.inclusion_tag('uploader_base.html')
def upload_file(obj):
    content_type = ContentType.objects.get_for_model(obj)
    object_id = obj.id

    return {'content_type_id': content_type.id, 'object_id': object_id}
