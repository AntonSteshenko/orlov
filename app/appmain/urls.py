
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from explane.views import CreateExplaneView, SuccessMessageView


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('explane/', CreateExplaneView.as_view(), name="explane"),
    path('success/', SuccessMessageView.as_view(), name="success"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
