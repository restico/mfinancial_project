from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest.serializers.users import UserSerializer
from rest_framework import generics, viewsets

from users.models import CustomUser


class UserModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer