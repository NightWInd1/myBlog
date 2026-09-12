from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', include(wagtailadmin_urls)),
    path('django-admin/', admin.site.urls),
    path('documents/', include(wagtaildocs_urls)),
    path('', include('blog.urls')),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
