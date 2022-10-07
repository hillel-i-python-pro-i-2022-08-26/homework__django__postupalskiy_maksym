from typing import NamedTuple
# from django.db import models


class UserInfo(NamedTuple):
    name: str
    password: str
    email: str

    def __str__(self):
        return f"Name: {self.name}. Email: {self.email}. Password: {self.password}"
