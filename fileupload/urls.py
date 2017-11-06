# encoding: utf-8
from django.conf.urls import url
from fileupload.views import *

urlpatterns = [

    url(r'^new/$', AttachmentCreateView.as_view(), name='upload-new'),
    url(r'^delete/(?P<pk>\d+)$', AttachmentDeleteView.as_view(), name='upload-delete'),
    url(r'^view/$', AttachmentListView.as_view(), name='upload-view')

]
