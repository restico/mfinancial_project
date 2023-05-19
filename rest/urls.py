from django.urls import path
from rest.views.transactions import *
from rest.views.users import *

urlpatterns = [
    path('transactions/', TransactionsListCreateAPIView.as_view(), name='transactions'),
    path('transactions/<int:pk>', TransactionsRetrieveUpdateDestroyView.as_view(), name='transactions-api'),
    path('deposits/', DepositsListCreateAPIView.as_view(), name='deposits'),
    path('deposits/<slug:slug>', DepositsRetrieveUpdateDestroyAPIView.as_view(), name='deposits-api'),
    path('credits/', CreditsListCreateAPIView.as_view(), name='credits'),
    path('credits/<slug:slug>', CreditsRetrieveUpdateDestroyAPIView.as_view(), name='credits-api'),
    path('user/', UserListCreateAPIView.as_view(), name='user'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-api'),
]
