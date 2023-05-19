from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from users.models import CustomUser


class Transactions(models.Model):
    class Meta:
        verbose_name = 'Транзакція'
        verbose_name_plural = 'Транзакції'

    categories = [
        ('food', 'Їжа'),
        ('shopping', 'Шопінг'),
        ('trip', 'Подорож'),
        ('education', 'Навчання'),
        ('accrual', 'Нарахування'),
        ('restaurant', 'Ресторани'),
        ('alcohol', 'Алкоголь'),
        ('health', 'Здоровя'),
        ('services', 'Послуги'),
        ('others', 'Інше'),
    ]

    statuses = [
        ('income', 'Дохід'),
        ('expense', 'Витрата')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Користувач', null=True)
    category = models.CharField(choices=categories, verbose_name='Категорія транзакції', null=True, max_length=16)
    status = models.CharField(max_length=16, choices=statuses, verbose_name='Статус транзакції', null=True)
    date = models.DateField(auto_now_add=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сума', null=True)

    def __str__(self):
        return f'Транзакція {self.user} з id - {self.pk}'
'''

    def save(self, *args, **kwargs):
        user = self.user

        if self.status == 'expense':
            user.wallet -= self.amount
        elif self.status == 'income':
            user.wallet += self.amount

        user.save()
        super().save(*args, **kwargs)'''


class Deposits(models.Model):
    slug = models.SlugField(unique=True, null=True, max_length=255, verbose_name='URL', )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, verbose_name='Користувач')
    name = models.CharField(verbose_name='Назва депозиту', max_length=225, null=True)
    percent = models.IntegerField(verbose_name='Процент множення депозиту', null=True)
    deposit_length = models.IntegerField(verbose_name='Кількість виплат')
    payed_times = models.IntegerField(verbose_name='Кількість теперішніх оплат', default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сума')

    class Meta:
        verbose_name = 'Депозит'
        verbose_name_plural = 'Депозити'

    def __str__(self):
        return f'Депозит {self.user} за назвою {self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Credits(models.Model):
    slug = models.SlugField(unique=True, null=True, max_length=255, verbose_name='URL')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, verbose_name='Користувач')
    name = models.CharField(verbose_name='Назва кредиту', max_length=225, null=True)
    percent = models.IntegerField(verbose_name='Процент множення кредиту', null=True)
    credit_length = models.IntegerField(verbose_name='Кількість необхідних оплат')
    payed_times = models.IntegerField(verbose_name='Кількість теперішніх оплат', default=0)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сума')


    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредити'

    def __str__(self):
        return f'Депозит {self.user} за назвою {self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

@receiver(post_save, sender=Credits)
def update_wallet(sender, instance, created, **kwargs, ):
    if created:
        user = instance.user
        user.wallet += instance.amount
        user.save()

