from django.db import models
from django.utils import timezone
from PIL import Image
from .forms import UploadFileForm
# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    pub_date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to = '')
    def save(self, **kwargs):
        black_and_white = kwargs.pop('black_and_white', False)
        instance = super(Post, self).save(**kwargs)
        if black_and_white:
            pil_image = Image.open(self.photo.url[1:])
            # black and white related code
            changed_image = pil_image.convert("L")
            changed_image.save(self.photo.url[1:])
        return instance