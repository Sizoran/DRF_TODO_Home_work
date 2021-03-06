from django.db import models


class User(models.Model):
    first_name = models.CharField(verbose_name="имя", max_length=64)
    last_name = models.CharField(verbose_name="фамилия",max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.CharField(verbose_name="почта",max_length=64, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

class Project(models.Model):
    name = models.CharField(verbose_name="уникальное название проекта", max_length=128, unique=True)
    link = models.CharField(verbose_name="ссылка на репозиторий", max_length=512, unique=True)
    description = models.TextField(verbose_name="описание проекта", blank=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.description

class TODO(models.Model):
    description = models.TextField(verbose_name='описание заметки',blank=True)
    created = models.DateTimeField(verbose_name="дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="дата обновления", auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.description
