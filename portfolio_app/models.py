from django.db import models

class PerfilHomepage(models.Model):    
    nome = models.CharField(max_length=200, blank=True, null=True)
    sobrenome = models.CharField(max_length=200, blank=True, null=True)   
    sobre_mim = models.TextField(blank=True, null=True)
    imagem_avatar = models.ImageField(null=True,
    blank=True, default="default.jpg")    
    ferramenta1 = models.ImageField(null=True, blank=True, default="default.jpg") 
    ferramenta2 = models.ImageField(null=True, blank=True, default="default.jpg") 
    ferramenta3 = models.ImageField(null=True, blank=True, default="default.jpg") 
    ferramenta4 = models.ImageField(null=True, blank=True, default="default.jpg") 
    ferramenta5 = models.ImageField(null=True, blank=True, default="default.jpg") 
    created = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return str(self.nome)

    class Meta:
        ordering = ['created']

    @property
    def imageURL(self):
        try:
            url = self.imagem_avatar.url
        except:
            url = ''
        return url