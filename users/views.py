from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView
from django.db.models import F
from django.shortcuts import redirect, get_object_or_404

from users.form import CustomUserCreationForm
from users.models import CustomUser
from tasks.models import Transactions, Deposits, Credits


class UserLoginView(LoginView):
    model = CustomUser
    form_class = AuthenticationForm
    template_name = 'user-html/login.html'

    def get_success_url(self):
        return reverse('profile', args=[self.request.user.pk])


class CreateProfileView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'user-html/register.html'

    def get_success_url(self):
        return reverse_lazy('login')


def logoutUser(request):
    logout(request)
    return redirect('login')


class ProfileView(DetailView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'user-html/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()

        categories = Transactions.categories
        category = self.request.GET.get('category')
        sort_order = self.request.GET.get('sort')
        status = self.request.GET.get('status')

        transactions = Transactions.objects.filter(user=self.request.user)
        if category:
            transactions = transactions.filter(category=category)
        if sort_order == 'asc':
            transactions = transactions.order_by('amount')
        if status:
            transactions = transactions.filter(status=status)
        elif sort_order == 'desc':
            transactions = transactions.order_by(F('amount').desc())

        deposits = Deposits.objects.filter(user=self.request.user)

        payment_from_deposits = []
        for deposit in deposits:
            payment = []
            if deposit.deposit_length == deposit.payed_times:
                dep = get_object_or_404(Deposits, pk=deposit.pk)
                dep.delete()
                continue
            income_amount = float(deposit.amount) * (int(deposit.percent) / 100)
            for i in range(1, deposit.deposit_length + 1):
                payment.append(f'Deposit income number {i} --- Income amount {income_amount}')
            payment_from_deposits.append(payment)

        deposits = list(zip(deposits, payment_from_deposits))

        credits = Credits.objects.filter(user=self.request.user)

        payment_for_all_credits = []
        for credit in credits:
            if credit.credit_length == credit.payed_times:
                cre = get_object_or_404(Credits, pk=credit.pk)
                cre.delete()
                continue
            payment_button = []
            payment = []
            amount_to_pay = (float(credit.amount) / int(credit.credit_length)) \
                            + float(credit.amount) / int(credit.credit_length) * (int(credit.percent) / 100)
            for i in range(1, credit.credit_length + 1):
                payment.append(f'Payment number {i} --- Payment amount {amount_to_pay} -- ')
                if i - 1 < credit.credit_length - credit.payed_times:
                    payment_button.append(True)
                else:
                    payment_button.append(False)

            payment = list(zip(payment, payment_button))
            payment_for_all_credits.append(payment)

        credits = list(zip(credits, payment_for_all_credits))

        user_wallet = CustomUser.objects.all()
        context['transactions'] = transactions
        context['categories'] = categories
        context['deposits'] = deposits
        context['credits'] = credits
        context['users'] = user_wallet
        context['payments'] = payment_for_all_credits

        return context


def increase_payed_times(request, pk):
    credits = get_object_or_404(Credits, pk=pk)
    user = credits.user
    user.wallet = float(user.wallet) - (float(credits.amount) / int(credits.credit_length)) \
                            + float(credits.amount) / int(credits.credit_length) * (int(credits.percent) / 100)
    user.save()
    credits.payed_times += 1
    credits.save()
    return redirect(reverse('profile', args=[credits.user.pk]))


def get_deposits(request, pk):
    deposits = get_object_or_404(Deposits, pk=pk)
    user = deposits.user
    user.wallet = float(user.wallet) + float(deposits.amount) * (float(deposits.percent) / 100.0)
    user.save()
    deposits.payed_times += 1
    deposits.save()
    return redirect(reverse('profile', args=[deposits.user.pk]))
