
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from mailings.views import ClientViewSet, MailingViewSet, MessageViewSet

from .yasg import swaggerurlpatterns


router = routers.DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'mailings', MailingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("admin/django-rq/", include("django_rq.urls")),
]

urlpatterns += swaggerurlpatterns
