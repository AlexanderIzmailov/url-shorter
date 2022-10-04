from venv import create
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CreateLink, MyRegisterUserForm
from django.urls import reverse_lazy, reverse
import random, string
from django.shortcuts import redirect
from .models import URL
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import MyTaskPermissionMixin


def generate_short_link():
    characters = string.ascii_letters + string.digits
    short_link = ''.join(random.choice(characters) for i in range(5))
    print("_______SHORT_LINK:_______", short_link)
    return short_link


# class LinkCreate2(SuccessMessageMixin, CreateView):
#     form_class = CreateLink
#     template_name = "create_link.html"
#     success_url = reverse_lazy('home')
#     link_short = generate_short_link();
#     success_message = 'Done! Short link: ' + link_short

#     def form_valid(self, form):
#         if self.request.user.is_authenticated:
#             form.instance.creator = self.request.user

#         form.instance.link_short = self.link_short
#         return super().form_valid(form)


def redirect_to(request, slug):
    link_item = URL.objects.get(link_short=slug)
    link_item.clicks_quantity += 1
    link_item.save()
    link_full = link_item.link_full
    return redirect(link_full)


# class Link(ListView):
#     model = URL
#     template_name = "index.html"


# class Link(SuccessMessageMixin, CreateView, ListView):
#     model = URL
#     template_name = "index.html"

#     form_class = CreateLink
#     template_name = "index.html"
#     success_url = reverse_lazy('home')
#     link_short = generate_short_link()
#     success_message = 'Done! Short link: ' + link_short

#     def form_valid(self, form):
#         if self.request.user.is_authenticated:
#             form.instance.creator = self.request.user

#         form.instance.link_short = self.link_short
#         return super().form_valid(form)


class LinkCreate(SuccessMessageMixin, CreateView):
    form_class = CreateLink
    template_name = "index.html"
    success_url = reverse_lazy('users_links')
    # link_short = generate_short_link()
    # success_message = 'Done! Short link: ' + link_short

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.creator = self.request.user

        self.link_short = generate_short_link()
        self.success_message = 'Done! Short link: ' + self.link_short
        self.request.session["new_link"] = self.link_short

        form.instance.link_short = self.link_short
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = URL.objects.all().order_by('-id')[:5]
        return context

    # def get_success_url(self):
    #     # return reverse('users_links', kwargs={'new_link': self.link_short})
    #     return reverse('users_links', "new_link"=self.link_short)


class UserCreate(SuccessMessageMixin, CreateView):
    form_class = MyRegisterUserForm
    template_name = "users_register.html"
    success_url = reverse_lazy('users_login')
    success_message = 'The user is registered'


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"
    next_page = reverse_lazy('home')
    success_message = "You're in!"

def logout_user(request):
    logout(request)
    messages.success(request, "You're out!")
    return redirect('home')


class Test(ListView):
    queryset = URL.objects.all()
    context_object_name = 'url_list'
    template_name = "test.html"


class UserLink(LoginRequiredMixin, ListView):
    context_object_name = 'url_list'
    template_name = "users_links.html"
    login_url = reverse_lazy('users_login')

    def get_queryset(self):
        user = self.request.user
        return URL.objects.filter(creator=user)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['new_link'] = "ASD"
    #     return context


class LinkDelete(MyTaskPermissionMixin, SuccessMessageMixin, DeleteView):
    model = URL
    template_name = "links_delete.html"
    success_url = reverse_lazy('users_links')
    success_message = 'The link has been removed'
