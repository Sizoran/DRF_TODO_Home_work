import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import ProjectModelViewSet
from .models import User as User1, TODO
import traceback



class TestProjectViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('api/Project')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUserDetailViewSet(TestCase):

    def test_get_user_detail(self):
        user = User1.objects.create(first_name='Adam', last_name='Smit', birthday_year=1799, email='Adam@mail.ru')
        client = APIClient()
        response = client.get(f'/generic/retrieveupdate/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestTODOViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/TODO/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestMixerTODO(APITestCase):

    def test_edit_admin(self):
        todo = mixer.blend(TODO)
        try:
            admin = User.objects.create_superuser(username='admin', email='admin@admin.com', password='admin123456')
        except Exception:
            print('Ошибка:\n', traceback.format_exc())
        self.client.login(username='admin', password='admin123456')
        response = self.client.patch(f'/api/TODO/{todo.id}/', {'description': 'Луноход 1, я Луноход 2'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = TODO.objects.get(id=todo.id)
        self.assertEqual(todo.description,'Луноход 1, я Луноход 2')
