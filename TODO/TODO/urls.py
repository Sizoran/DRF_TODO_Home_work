"""TODO URL Configuration

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
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from mainapp.views import ProjectModelViewSet, TODOModelViewSet, UserListAPIView ,UserRetrieveUpdateAPIView
from mainapp import views
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView



router = DefaultRouter()
router.register('Project', ProjectModelViewSet)
router.register('TODO', TODOModelViewSet)



schema_view = get_schema_view(
    openapi.Info(
        title="ToDo",
        default_version='0.1',
        description="Данный проект создан для постижения DRF и оттачивания навыком ображения с API!",
        contact=openapi.Contact(email="89024848835@bk.ru"),
        license=openapi.License(name="MIT License"),
    ),
     public=True,
     permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('views/api-view/', UserListAPIView.as_view()),
    path('generic/retrieveupdate/<int:pk>/', UserRetrieveUpdateAPIView.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
]