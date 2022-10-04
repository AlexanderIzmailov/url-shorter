"""url_shorter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from url_shorter import views
from .views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', TemplateView.as_view(template_name="index.html"), name='home'),
    # path('', views.Link.as_view(), name='home'),
    path('', views.LinkCreate.as_view(), name='home'),
    # path('last/', views.Last.as_view(), name='last'),
    # path('create/', views.LinkCreate.as_view(), name='links_create'),
    path('r/<slug:slug>/', views.redirect_to, name='redirect'),
    path('users/create/', views.UserCreate.as_view(), name='users_create'),
    path('login/', views.LoginUser.as_view(), name='users_login'),
    path('logout/', views.logout_user, name='users_logout'),
    path('test/', views.Test.as_view(), name='test'),
    path('mylinks/', views.UserLink.as_view(), name='users_links'),
    path('links/<int:pk>/delete/', views.LinkDelete.as_view(), name='links_delete'),
]
