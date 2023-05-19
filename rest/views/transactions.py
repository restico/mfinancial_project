from rest.serializers.transactions import *
from tasks.models import *
from rest_framework import generics, viewsets

class TransactionModelViewSet(viewsets.ModelViewSet):

    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer


class DepositModelViewSet(viewsets.ModelViewSet):
    queryset = Deposits.objects.all()
    serializer_class = DepositsSerializer


class CreditsModelViewSet(viewsets.ModelViewSet):
    queryset = Credits.objects.all()
    serializer_class = CreditsSerializer


class TransactionsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer


class TransactionsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transactions.objects.all()
    serializer_class = TransactionsSerializer


class DepositsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Deposits.objects.all()
    serializer_class = DepositsSerializer


class DepositsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'

    queryset = Deposits.objects.all()
    serializer_class = DepositsSerializer


class CreditsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Credits.objects.all()
    serializer_class = CreditsSerializer


class CreditsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'

    queryset = Credits.objects.all()
    serializer_class = CreditsSerializer
