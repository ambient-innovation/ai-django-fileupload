# encoding: utf-8
import mimetypes
import re

from django.core.urlresolvers import reverse
from django.conf import settings

from fileupload import constants


def order_name(name):
    """order_name -- Limit a text to 20 chars length, if necessary strips the
    middle of the text and substitute it for an ellipsis.

    name -- text to be limited.

    """
    name = re.sub(r'^.*/', '', name)
    if len(name) <= 20:
        return name
    return name[:10] + "..." + name[-7:]


def serialize(instance, file_attr='file'):
    """serialize -- Serialize a Picture instance into a dict.

    instance -- Picture instance
    file_attr -- attribute name that contains the FileField or ImageField

    """
    obj = getattr(instance, file_attr)
    mimetype = mimetypes.guess_type(obj.path)[0] or 'image/png'
    if re.match(r'image', mimetype):
        # We can only really display the thumbnail, if it is an image
        thumbnail_url = obj.url
    else:
        # Otherwise we will display a default placeholder image
        if hasattr(settings, 'UPLOADER_DEFAULT_THUMBNAIL'):
            thumbnail_url = settings.UPLOADER_DEFAULT_THUMBNAIL
        else:
            thumbnail_url = constants.UPLOADER_DEFAULT_THUMBNAIL

    return {
        'url': obj.url,
        'name': order_name(obj.name),
        'type': mimetype,
        'thumbnailUrl': thumbnail_url,
        'size': obj.size,
        'deleteUrl': reverse('upload-delete', args=[instance.pk]),
        'deleteType': 'DELETE',
    }


