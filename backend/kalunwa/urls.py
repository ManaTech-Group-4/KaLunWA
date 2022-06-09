"""kalunwa URL Configuration

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
from django.urls import path, include
from django.conf import settings
# to be used for url patterns
from django.conf.urls.static import static
from kalunwa.users.views import CustomObtainTokenPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

# add /api to access api's

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include(
        [
            path('token/', CustomObtainTokenPairView.as_view(), name='token-obtain-pair'),
            path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
            path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),                
            path('', include('kalunwa.content.urls')),
            path('users/', include('kalunwa.users.urls')),              
            path('', include('kalunwa.page_containers.urls')),                  
        ]
        )
    )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)