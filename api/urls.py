from api.spectaculars.urls import urlpatterns as docs
from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt'))
]

urlpatterns += docs