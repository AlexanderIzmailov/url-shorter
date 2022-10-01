from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


class MyTaskPermissionMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().creator.id is not request.user.id and not request.user.is_superuser:
            # return HttpResponse("Permission's error")
            messages.error(request, "You have no access to delete another user's links")
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
