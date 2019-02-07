from . import views
from django.urls import path,re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index),
]