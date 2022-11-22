from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users_admin.forms import UserRegistrationForm
from users_admin.models import Admin


class UserSingUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    template_name = "users/singup.html"

    class Meta:
        model = Admin
        fields = (
            "username",
            "avatar",
        )


class UserUpdateView(UpdateView):
    model = Admin
    fields = (
        "username",
        "avatar",
    )
    template_name = "users/user_update_form.html"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("home_page:index")
