"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.index, name='index')
Class-based views
    1. Add an import:  from other_app.views import index
    2. Add a URL to urlpatterns:  path('', index.as_view(), name='index')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
import jobs.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", jobs.views.index, name="index"),
    path("portfolio/", jobs.views.portfolio, name="portfolio"),
    path("about/", jobs.views.about, name="about"),
    path("contact/", jobs.views.contact, name="contact"),
    path("header/", jobs.views.header, name="header"),
    path("footer/", jobs.views.footer, name="footer"),
    path("base/", jobs.views.base, name="base"),
    path("jobs/<int:job_id>", jobs.views.detail, name="detail"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
