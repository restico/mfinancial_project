from django.contrib import admin
from tasks.models import *


@admin.register(Transactions)
class TransactionModel(admin.ModelAdmin):
    list_display = ('pk', 'user')


@admin.register(Deposits)
class DepositsModel(admin.ModelAdmin):
    list_display = ('slug', 'user')


@admin.register(Credits)
class CreditsModel(admin.ModelAdmin):
    list_display = ('slug', 'user')
