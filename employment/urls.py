"""employment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/social_auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('api/swagger/', get_swagger_view(title='Employment API')),
    path('api/auth/', include('core.api.urls')),
    path('api/summaries/', include('summary.api.urls')),
    path('api/companies/', include('company.api.urls')),
    path('api/hiring/', include('hiring.api.urls')),
    path('api/freelance/', include('freelance.api.urls')),
    path('', lambda x: redirect('/admin/')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)