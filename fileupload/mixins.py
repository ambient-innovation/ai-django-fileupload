from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

from fileupload.constants import UPLOADER_LOGIN_REQUIRED


class CustomAccessMixin(LoginRequiredMixin):
    raise_exception = True

    def dispatch(self, request, *args, **kwargs):

        def is_login_required():
            if hasattr(settings, 'UPLOADER_LOGIN_REQUIRED'):
                return settings.UPLOADER_LOGIN_REQUIRED
            return UPLOADER_LOGIN_REQUIRED

        if is_login_required() and not request.user.is_authenticated:
            return self.handle_no_permission()

        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
