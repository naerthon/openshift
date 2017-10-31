from django.conf.urls import url, include
from django.contrib import admin
from apps.core import urls as core_urls
from apps.accounts import urls as accounts_urls
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(core_urls, namespace='core')),
    url(r'^', include(accounts_urls, namespace='accounts')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)