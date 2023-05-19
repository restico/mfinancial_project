from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest.views.transactions import *
from rest.views.users import *

router = DefaultRouter()
router.register('transactions', TransactionModelViewSet)
router.register('deposits', DepositModelViewSet)
router.register('credits', CreditsModelViewSet)
router.register('user', UserModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include('api.urls')),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')), #re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/models', include(router.urls)),
]

urlpatterns += [
    path('', include('main.urls')),
    path('user/', include('users.urls')),
    path('transactions/', include('tasks.urls'))
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
