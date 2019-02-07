from django.db import models
from django.utils import timezone
from PIL import Image
from .forms import UploadFileForm
# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to = '')
    share = models.BooleanField(default=False)