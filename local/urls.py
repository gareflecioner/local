
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [   
path('admin/', admin.site.urls),
path('again/', include('again.urls')),
path('', RedirectView.as_view(url='/again/', permanent=True)), 
#path('accounts/', include('django.contrib.auth.urls')),
path('users/', include('users.urls', namespace="users")),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
