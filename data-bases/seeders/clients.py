from faker import Faker
from uuid import uuid4


faker = Faker(["es_CO"])

for _ in range(1000000):
    email = faker.email()
    name = faker.name()
    phone = faker.phone_number()
    identification_number = uuid4()
    print(f'{name},{email},{phone},{identification_number}')