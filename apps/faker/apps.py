from faker import Faker

fake = Faker()


def faker_name() -> str:
    return str(fake.first_name())
