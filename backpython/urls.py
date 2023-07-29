"""
URL configuration for backpython project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from api.views import DriveCreateView, DriveLoginView, DriverListView, DriverUpdateView, UserCreateView, UserDetailView, UserListView, UserLoginView, UserUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/create/', UserCreateView.as_view(), name='user-login'),
    path('api/user/login/', UserLoginView.as_view(), name='user-login'),
    path('api/driver/create/', DriveCreateView.as_view(), name='driver-create'),
    path('api/driver/login/', DriveLoginView.as_view(), name='driver-login'),

    # auth token done now otop etc left
    path('api/users/list', UserListView.as_view(), name='user-list'),
    path('api/drivers/list', DriverListView.as_view(), name='driver-list'),
    path('api/users/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('api/drivers/<int:pk>/', DriverUpdateView.as_view(), name='driver-update'),
    path('api/usersdetail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    
    
    
]
