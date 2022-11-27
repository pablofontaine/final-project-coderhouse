from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class New(models.Model):

    def get_user_id(request):
        return print(request.user.username)

    title = models.CharField(max_length=140, null=False, blank=False, verbose_name='Título')
    subtitle = models.CharField(max_length=280, null=False, blank=False, verbose_name='Subtítulo')
    description = models.TextField(max_length=980, null=False, blank=True, verbose_name='Descripción')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última modificación')

    class Meta:
        unique_together = ()
        ordering = ['-created_at']

    def __str__(self):
        return f'Codigo: {self.id} | Autor: {self.author.first_name} {self.author.last_name} | Título: {self.title}'