from venv import create
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CreateLink
from django.urls import reverse_lazy
import random, string
from django.shortcuts import redirect
from .models import URL

def generate_short_link():
    characters = string.ascii_letters + string.digits
    short_link = ''.join(random.choice(characters) for i in range(5))
    return short_link


class LinkCreate(SuccessMessageMixin, CreateView):
    form_class = CreateLink
    template_name = "create_link.html"
    success_url = reverse_lazy('home')
    link_short = generate_short_link();
    success_message = 'Done! Short link: ' + link_short

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.creator = self.request.user

        form.instance.link_short = self.link_short
        return super().form_valid(form)


def redirect_to(request, slug):
    link_item = URL.objects.get(link_short=slug)
    link_item.clicks_quantity += 1
    link_item.save()
    link_full = link_item.link_full
    return redirect(link_full)