from django.contrib import admin
from .models import Admin
from django.contrib.auth.admin import UserAdmin


admin.site.register(Admin, UserAdmin)
