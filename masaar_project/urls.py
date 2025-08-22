# masaar_project/urls.py
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from .settings import BASE_DIR

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("villas.urls", "villas"), namespace="villas")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / "villas" / "static")
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
