"""company_roles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from company_roles.api.views import RegistrationView, LoginView, ListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('api/auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register', UserRegistrationView.as_view(), name='register'),
    path('api/auth/login', UserLoginView.as_view(), name='login'),
    path('api/auth/users', UserListView.as_view(), name='users'),
]
