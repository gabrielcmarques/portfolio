from django.db import models
from django.contrib.auth.models import User
import uuid


class Perfil(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    sobrenome = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    endereço = models.CharField(max_length=200, blank=True, null=True)    
    bio = models.TextField(blank=True, null=True)
    imagem_perfil = models.ImageField(null=True,
    blank=True, default="default.jpg")   
    social = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)    
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.imagem_perfil.url
        except:
            url = ''
        return url

        
class Projeto(models.Model):
    owner = models.ForeignKey(
    Perfil, null=True, blank=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descricao = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(null=True,
    blank=True, default="default.jpg")
    imagem_demo = models.ImageField(null=True,
    blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)   
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['created']

    @property
    def thumbnailURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url


class Tag(models.Model):
    nome = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.nome