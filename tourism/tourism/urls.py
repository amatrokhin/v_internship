"""tourism URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from rest_api import views


# register links for serializers
router = routers.DefaultRouter()
router.register(r'pereval_added', views.PerevalAddedViewset, basename='pereval_added')
router.register(r'pereval_areas', views.PerevalAreasViewset, basename='pereval_areas')
router.register(r'pereval_images', views.PerevalImagesViewset, basename='pereval_images')
router.register(r'spr_activities_types', views.SprActivitiesTypesViewset, basename='spr_activities_types')
router.register(r'coords', views.CoordsViewset, basename='coords')
router.register(r'users', views.UsersViewset, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # inclide links for REST API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('rest_api.urls'))
]
