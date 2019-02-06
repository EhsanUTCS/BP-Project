from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.static import serve
from .models import Post
from django.db import models
from PIL import Image
from io import BytesIO
import os
# Create your views here.

def index(request):
    return render(request, 'feed/index.html')

def upload_img(request):
    if request.method == 'POST' and request.FILES['photo']:
        img = request.FILES['photo']
        post = Post(name=img.name, photo=img)
        post.save()
        request.session['photo_pk'] = post.pk
        context = {
            'post': post
        }
        return render(request, 'peditor/editor.html', context = context)

def using_tools (request):
    post = Post.objects.get(pk = request.session['photo_pk'])
    post.save(black_and_white = True, update_fields = ['photo'])
    return render(request, 'peditor/editor.html', {
        'post' : post
    })

