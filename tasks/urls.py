from django.urls import path
from tasks.views import *
from users.views import increase_payed_times, get_deposits

urlpatterns = [
    path('transaction/create/', TransactionCreateView.as_view(), name='create-transactions'),
    path('transaction/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transaction/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),

    path('deposits/create', DepositsCreateView.as_view(), name='create-deposits'),
    path('deposits/<int:pk>/delete', DepositsDelete.as_view(), name='delete-deposit'),
    path('credits/create', CreditsCreateView.as_view(), name='create-credits'),
    path('credits/<int:pk>/', CreditsDelete.as_view(), name='delete-credits'),

    path('increase_payed_times/<int:pk>/', increase_payed_times, name='increase_payed_times'),
    path('get_deposits/<int:pk>/', get_deposits, name='get_deposits')
]