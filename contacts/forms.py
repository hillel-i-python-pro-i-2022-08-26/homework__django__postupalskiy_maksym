from django import forms
from django.core.exceptions import ValidationError
from core import settings
from .models import Contact


class AddContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["b_day"].input = settings.DATE_INPUT_FORMATS
        self.fields["b_day"].help_txt = "format DD.MM.YYYY"
        self.fields["phone"].help_txt = "Enter phone number"

    class Meta:
        model = Contact
        fields = ("name", "phone", "b_day")

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not phone.isdecimal():
            raise ValidationError("Invalid phone number(int only)")
        elif len(phone) != 10:
            raise ValidationError("Invalid phone number(enter UA number")
        elif not phone.startswith("0"):
            raise ValidationError("Invalid phone number(should starts with 0)")
        return phone
