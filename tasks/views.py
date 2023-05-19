from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import reverse

from tasks.forms import TransactionForm
from tasks.models import Transactions, Deposits, Credits
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView, UpdateView


class TransactionCreateView(CreateView):
    model = Transactions
    fields = ['category', 'status', 'amount']
    template_name = 'transactions-html/transaction-create.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user = self.request.user

        if transaction.status == 'expense':
            transaction.user.wallet -= transaction.amount
        elif transaction.status == 'income':
            transaction.user.wallet += transaction.amount

        transaction.user.save()
        transaction.save()
        return super().form_valid(form)


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transactions
    template_name = 'transactions-html/transaction_confirm_delete.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def get_queryset(self):
        # Обмежте запит до транзакцій поточного користувача
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transactions
    form_class = TransactionForm
    template_name = 'transactions-html/transaction-update.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def get_queryset(self):
        # Обмежте запит до транзакцій поточного користувача
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class DepositsCreateView(CreateView):

    model = Deposits
    fields = ('name', 'percent', 'deposit_length', 'amount')
    template_name = 'transactions-html/deposits-create.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user = self.request.user
        transaction.save()
        return super().form_valid(form)


class DepositsDelete(LoginRequiredMixin, DeleteView):
    model = Deposits
    template_name = 'transactions-html/deposits_confirm_delete.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class CreditsCreateView(CreateView):

    model = Credits
    fields = ('name', 'percent', 'credit_length', 'amount')
    template_name = 'transactions-html/credits-create.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user = self.request.user
        transaction.save()
        return super().form_valid(form)


class CreditsDelete(LoginRequiredMixin, DeleteView):
    model = Credits
    template_name = 'transactions-html/credits_confirm_delete.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

