from httplib2 import Response
from rest_framework.viewsets import ModelViewSet
from mainapp.models import Project, TODO, User
from mainapp.serializers import ProjectModelSerializer, TODOModelSerializer, UserModelSerializer
from mainapp.filters import ProjectFilter, TODOFilter
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination

class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
    filerset_class = TODOFilter
    pagination_class = TODOLimitOffsetPagination

    def destroy(self, request, pk=None, *args, **kwargs):
        queryset = get_object_or_404(TODO, pk=pk)
        queryset.hiden = False
        queryset.save()
        content = {'Запись изменена'}
        return Response(content, status=200)


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer