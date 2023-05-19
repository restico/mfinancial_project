from django.urls import path
from users.views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', CreateProfileView.as_view(), name='register'),
    path('logout/', logoutUser, name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile')
]