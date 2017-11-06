import json

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase

from fileupload.tests.test_utils import build_url
from model_mommy import mommy


class AttachmentListViewTests(TestCase):
    def setUp(self):
        """
        Set up all the tests
        """
        self.user = mommy.make(User)
        self.content_type_user = ContentType.objects.get(model="user")
        self.attachments = mommy.make('fileupload.Attachment',
                                      content_type=self.content_type_user,
                                      object_id=self.user.id,
                                      _create_files=True,
                                      _quantity=3)

    def test_show_all_attachments(self):
        """
        All existent attachments should be retrieved
        """
        response = self.client.get(build_url('upload-view', get={'content_type_id': self.content_type_user.id,
                                                                 'object_id': self.user.id}),
                                   HTTP_ACCEPT='application/json')
        response_files = json.loads(response.content)['files']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response_files), len(self.attachments))
