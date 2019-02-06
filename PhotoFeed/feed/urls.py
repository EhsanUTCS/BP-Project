from . import views
from django.urls import path,re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index),
    path('upload', views.upload_img, name='upload'),
    path('upload/$', views.using_tools, name='using_tools'),
]