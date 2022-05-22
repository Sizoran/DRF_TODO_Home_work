from rest_framework.viewsets import ModelViewSet
from mainapp.models import Project, TODO, User
from mainapp.serializers import ProjectModelSerializer, TODOModelSerializer, UserModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer