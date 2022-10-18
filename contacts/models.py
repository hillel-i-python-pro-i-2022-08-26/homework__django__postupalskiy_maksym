from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.SlugField(max_length=60)
    b_day = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    is_auto_generated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.phone} {self.b_day}"

    __repr__ = __str__

    class Meta:
        ordering = ('-created_at',)
