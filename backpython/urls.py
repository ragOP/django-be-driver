from django.contrib import admin
from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from api.views import DriveCreateView, DriveLoginView, DriverListView, DriverUpdateView, UserCreateView, UserDetailView, UserListView, UserLoginView, UserUpdateView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/create/', UserCreateView.as_view(), name='user-login'),
    path('api/user/login/', UserLoginView.as_view(), name='user-login'),
    path('api/driver/create/', DriveCreateView.as_view(), name='driver-create'),
    path('api/driver/login/', DriveLoginView.as_view(), name='driver-login'),
# s
    # auth token done now otop etc lefts
    path('api/users/list', UserListView.as_view(), name='user-list'),
    path('api/drivers/lists', DriverListView.as_view(), name='driver-list'),
    path('api/users/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('api/drivers/<int:pk>/', DriverUpdateView.as_view(), name='driver-update'),
    path('api/usersdetail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
]
