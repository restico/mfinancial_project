from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    slug = models.SlugField(unique=True, verbose_name='URL')
    wallet = models.DecimalField(verbose_name='Сума акаунта', null=True, max_digits=15, decimal_places=2, default=1000)

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

    def __str__(self):
        return f'{self.username} account'

