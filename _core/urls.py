"""
URL configuration for _core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from a_home.views import *
from a_users.views import profile_view

admin.site.site_header = f"{settings.UNFOLD['SITE_TITLE']} Admin Dashboard"
admin.site.site_title = settings.UNFOLD['SITE_HEADER']
admin.site.index_title = "Last Code Update: 20th May 26 22:00"

urlpatterns = [
    path('admin/', include('admin_honeypot.urls'), name='admin_honeypot'),
    path('enter/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home_view, name="home"),
    path('profile/', include('a_users.urls')),
    path('@<username>/', profile_view, name="profile"),
]

# Only used in development, whitenoise can serve files when DEBUG=False
if settings.DEBUG and settings.ENVIRONMENT == 'development':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
    ]
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns = urlpatterns + debug_toolbar_urls()
