
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [   re_path('admin/', admin.site.urls),
re_path('again/', include('again.urls')),path('',
RedirectView.as_view(url='/again/', permanent=True)), ] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)