# encoding: utf-8
import json

from django.http import HttpResponse
from django.views.generic import CreateView, DeleteView, ListView
from fileupload.mixins import CustomAccessMixin

from .models import Attachment
from .response import JSONResponse, response_mimetype
from .serialize import serialize


class AttachmentCreateView(CustomAccessMixin, CreateView):
    model = Attachment
    fields = "__all__"

    def form_valid(self, form):
        self.object = form.save()
        files = [serialize(self.object)]
        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        # response = HttpResponse(json.dumps(data), content_type="application/json")
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def form_invalid(self, form):
        data = json.dumps(form.errors)
        return HttpResponse(content=data, status=400, content_type='application/json')


class AttachmentDeleteView(CustomAccessMixin, DeleteView):
    model = Attachment

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        response = JSONResponse(True, mimetype=response_mimetype(request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response


class AttachmentListView(CustomAccessMixin, ListView):
    model = Attachment

    def render_to_response(self, context, **response_kwargs):
        files = [serialize(p) for p in self.get_queryset().filter(content_type=self.request.GET['content_type_id'],
                                                                  object_id=self.request.GET['object_id'])]

        data = {'files': files}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response
