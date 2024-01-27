from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)