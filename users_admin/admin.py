from django.contrib import admin
from django.contrib.auth import get_user_model


from .forms import UserRegistrationForm
from .models import Admin
from django.contrib.auth.admin import UserAdmin


class UserRegister(UserAdmin):
    add_form = UserRegistrationForm
    form = UserRegistrationForm
    model = get_user_model()
    list = ["email", "password"]


admin.site.register(Admin, UserAdmin)
