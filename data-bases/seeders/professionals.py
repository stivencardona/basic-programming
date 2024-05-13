from faker import Faker
import random

faker = Faker(["es_CO"])


for _ in range(3000):
    email = faker.email()
    name = faker.name()
    phone = faker.phone_number()
    type = random.randint(1, 3)
    print(f'{name},{email},{phone},{type}')