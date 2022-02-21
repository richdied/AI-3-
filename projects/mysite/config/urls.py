from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'common'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)