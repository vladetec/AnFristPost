from django.contrib.auth.models import User
from django.db import models
import uuid
from stdimage.models import StdImageField
from django.urls import reverse


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

"""
class Base(models.Model):
    created = models.DateTimeField('Criação',auto_now_add=True)
    updated = models.DateTimeField('Atualização',auto_now=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True
"""



class Post(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60, unique=True, null=True, blank=True,)
    sub_title = models.CharField(max_length=60)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True,)
    imagem = StdImageField('Imagem', upload_to=get_file_path, null=True,
     blank=True, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True,)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField('Ativo?', default=True) 
    
    class Meta:
        verbose_name = 'Titulo'
        verbose_name_plural = 'Titulos'
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.sub_title    

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

