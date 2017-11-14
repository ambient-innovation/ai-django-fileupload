# encoding: utf-8
import os
import uuid

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _

from fileupload.constants import UPLOADER_UPLOAD_DIRECTORY


def upload_to(instance, file_name):
    file_new_name = "{0}.{1}".format(uuid.uuid4().hex, file_name.split('.')[-1])
    file_dir = os.path.join(UPLOADER_UPLOAD_DIRECTORY, file_new_name)
    while Attachment.objects.filter(file=file_dir):
        upload_to(instance, file_name)

    return file_dir


class CommonInfo(models.Model):
    created_at = models.DateTimeField(_(u"Created at"), default=now, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Created by"), blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_created", on_delete=models.SET_NULL)
    last_modified_at = models.DateTimeField(_(u"Last modified at"), default=now, blank=True)
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_(u"Last modified by"), blank=True,
                                         null=True, related_name="%(app_label)s_%(class)s_lastmodified",
                                         on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = now()

        self.last_modified_at = now()
        super(CommonInfo, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Attachment(CommonInfo):
    file = models.FileField(_(u"File"), upload_to=upload_to)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = fields.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _(u"Attachment")
        verbose_name_plural = _(u"Attachments")

    def __str__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        super(Attachment, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """delete -- Remove to leave file."""
        self.file.delete(False)
        super(Attachment, self).delete(*args, **kwargs)
