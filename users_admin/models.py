from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
import uuid


def get_user_icon_path(instance, filename) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"users/user/avatar/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class Admin(AbstractUser):
    avatar = models.ImageField(
        max_length=255,
        blank=True,
        null=True,
        upload_to=get_user_icon_path,
    )

    def get_absolute_url(self):
        return reverse(
            "users:edit",
            kwargs={"pk": self.pk},
        )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Admin"
