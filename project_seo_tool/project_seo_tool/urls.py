
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView

from project_seo_tool import settings
from app_seo_tool import urls as app_seo_urls

admin.site.site_header = 'CG3 SEO'
admin.autodiscover()

urlpatterns = [

    # Redirect
    path('', RedirectView.as_view(url='/panel/home/')),

    # App Urls
    path('panel/', include((app_seo_urls, 'panel'), namespace='panel')),

    # Admin Urls
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
