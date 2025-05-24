from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('partners/', include('partners.urls')),
    path('api/', include('api.urls')),
]

# Обслуживание статичних и медиа файлов (работает и в DEBUG=False)
if settings.DEBUG or True:  # Принудительно включаем для тестирования
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])