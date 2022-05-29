from django.contrib import admin
from mainapp.models import Project, TODO, User

# Register your models here.
admin.site.register(Project)
admin.site.register(TODO)
admin.site.register(User)