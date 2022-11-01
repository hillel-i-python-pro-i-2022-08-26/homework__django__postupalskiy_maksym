from faker import Faker
from typing import TypeAlias, Iterator
from datetime import datetime
from random import randint, choice
from contacts.models import Contact

fake = Faker()

PHONE_NUMBER: TypeAlias = str
BIRTHDAY: TypeAlias = datetime.date


def number_generator() -> PHONE_NUMBER:
    num_code = ["99", "93", "97", "63", "66", "67", "68", "99", "99"]
    number = randint(1000000, 9999999)
    return f"+380{choice(num_code)}{number}"


def b_day_generator() -> BIRTHDAY:
    year = randint(1900, 2009)
    month = randint(1, 12)
    day = randint(1, 28)
    return f"{year}-{month}-{day}"


def return_contact(amount: int = 10) -> Iterator[Contact]:
    for _ in range(amount):
        yield Contact(
            name=fake.first_name(),
            phone=number_generator(),
            b_day=b_day_generator(),
        )
