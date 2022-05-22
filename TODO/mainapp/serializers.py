from rest_framework.serializers import HyperlinkedModelSerializer
from mainapp.models import Project, TODO, User

class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TODOModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'

class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
