from email.policy import default
from django.db import models

class Artigo(models.Model):
    titulo = models.CharField(max_length=250, null=True, blank=True, editable=True, default='NONE')
    url = models.URLField(max_length=250, default='', editable=True)
    checkmark = models.BooleanField(default=False, editable=True)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo