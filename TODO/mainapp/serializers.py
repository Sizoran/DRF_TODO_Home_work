from rest_framework.serializers import HyperlinkedModelSerializer,ModelSerializer
from mainapp.models import Project, TODO, User

class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TODOModelSerializer(ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
