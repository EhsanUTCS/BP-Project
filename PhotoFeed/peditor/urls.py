from . import views
from django.urls import path

urlpatterns = [
    path('', views.upload_img, name='upload'),
    path('BW', views.black_and_white, name='black_and_white'),
    path('CRP', views.crop, name='crop'),
    path('RSZ', views.resize, name='resize'),
    path('RT', views.rotate, name='rotate'),
    path('share/success', views.share, name='share'),
]
