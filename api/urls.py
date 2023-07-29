from django.contrib import admin
from django.urls import path,include
from api.views import UserCreateView
from rest_framework import routers


router= routers.DefaultRouter()
router.register(r'login',UserCreateView)

urlpatterns = [
    path('',include(router.urls))
    
]
