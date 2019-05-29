from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Manager, Users, Organization

admin.site.register(Manager)
admin.site.register(Users)
admin.site.register(Organization)
