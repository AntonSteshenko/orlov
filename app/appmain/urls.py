
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from explane.views import CreateExplaneView


urlpatterns = [
    

    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('explane/', CreateExplaneView.as_view(), name="explane")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
