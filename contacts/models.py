import uuid
from django.db import models
from django.urls import reverse


def get_icon_path(instance, filename) -> str:
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"contacts/contact/avatar/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.SlugField(max_length=60)
    b_day = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    is_auto_generated = models.BooleanField(default=False)
    avatar = models.ImageField(
        max_length=255,
        blank=True,
        null=True,
        upload_to=get_icon_path,
    )

    def __str__(self):
        return f"{self.name} {self.phone} {self.b_day}"

    __repr__ = __str__

    def get_absolute_url(self):
        return reverse(
            "contacts:contact_update",
            kwargs={"pk": self.pk},
        )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
