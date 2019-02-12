from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
from feed.models import Post
from .forms import Crop_Form
from feed.forms import UploadFileForm
# Create your views here.

def upload_img(request):
    if not request.FILES:
        return render(request, 'feed/index.html', {
            'error_message': "You Should Choose A File Before Upload",
            'posts' : Post.objects.filter(share=True).order_by('-pub_date'),
        })
    if request.method == 'POST':
        img = request.FILES['photo']
        post = Post(name=img.name, photo=img)
        post.save()
        request.session['photo_pk'] = post.pk
        context = {
            'post': post,
            'crop_form': Crop_Form
        }
        return render(request, 'peditor/editor.html', context = context)

def black_and_white (request):
    post = Post.objects.get(pk = request.session['photo_pk'])
    pil_image = Image.open(post.photo.url[1:])
    # black and white related code
    changed_image = pil_image.convert("L")
    changed_image.save(post.photo.url[1:])
    post.save(update_fields = ['photo'])
    return render(request, 'peditor/editor.html', {
        'post' : post
    })

def crop (request):
    post = Post.objects.get(pk = request.session['photo_pk'])
    pil_image = Image.open(post.photo.url[1:])
    # form = Crop_Form(request.POST, request.FILES)
    try:
        # crop related code
        a = int(request.POST.get('left'))
        b = int(request.POST.get('upper'))
        c = int(request.POST.get('right'))
        d = int(request.POST.get('lower'))
        if c >= a or d >= b or c == d or a == b:
            raise SystemError
        elif a < 0 or b < 0 or c < 0 or d < 0:
            return render(request, 'peditor/editor.html', {
            'post' : post,
            'error_message' : "Values Must be > 0"
            })
        else:
            changed_image = pil_image.crop((a, b, c, d))
            changed_image.save(post.photo.url[1:])
            post.save(update_fields = ['photo'])
            return render(request, 'peditor/editor.html', {
            'post' : post,
            })
    except ValueError:
        return render(request, 'peditor/editor.html', {
            'post' : post,
            'error_message' : "You Must Fill All Fields"
        })
    except SystemError:
        return render(request, 'peditor/editor.html', {
            'post' : post,
            'error_message' : "Tile Cannot Extend Out of Image",
        })
    return render(request, 'peditor/editor.html', {
        'post' : post
    })

def resize (request):
    post = Post.objects.get(pk = request.session['photo_pk'])
    pil_image = Image.open(post.photo.url[1:])
    # form = Crop_Form(request.POST, request.FILES)
    if request.POST.get('width') != '' and request.POST.get('height') != '':
        # crop related code
        try:
            width = int(request.POST.get('width'))
            height = int(request.POST.get('height'))
            changed_image = pil_image.resize((width, height))
            changed_image.save(post.photo.url[1:])
            post.save(update_fields = ['photo'])
        except ValueError:
            return render(request, 'peditor/editor.html', {
            'post' : post,
            'error_message' : "Values Must be > 0"
        })
    else:
        return render(request, 'peditor/editor.html', {
            'post' : post,
            'error_message' : "You Must Fill All Fields"
        })
    return render(request, 'peditor/editor.html', {
        'post' : post
    })

def rotate (request):
    post = Post.objects.get(pk = request.session['photo_pk'])
    pil_image = Image.open(post.photo.url[1:])
    # form = Crop_Form(request.POST, request.FILES)
    if request.POST.get('angle') != '':
        # crop related code
        angle = int(request.POST.get('angle'))
        changed_image = pil_image.rotate(angle, expand=1)
        changed_image.save(post.photo.url[1:])
        post.save(update_fields = ['photo'])
    else:
        return render(request, 'peditor/editor.html', {
            'post' : post,
            'error_message' : "You Must Fill All Fields"
        })
    return render(request, 'peditor/editor.html', {
        'post' : post
    })

def share (request):
    post = Post.objects.get(pk = request.session['photo_pk'])
    post.share = True
    post.save()
    return render(request, 'feed/index.html', {
        'posts' : Post.objects.filter(share=True).order_by('-pub_date')
    })
