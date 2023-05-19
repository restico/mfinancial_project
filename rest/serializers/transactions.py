from django.contrib.auth.models import User
from rest_framework import serializers
from tasks.models import *

class TransactionsSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=CustomUser.objects.all())

    class Meta:
        model = Transactions
        fields = '__all__'

class DepositsSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=CustomUser.objects.all())
    class Meta:
        model = Deposits
        fields = '__all__'


class CreditsSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=CustomUser.objects.all())

    class Meta:
        model = Credits
        fields = '__all__'
