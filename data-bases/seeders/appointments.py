from faker import Faker
from datetime import datetime
from random import randint

faker = Faker(["es_CO"])

end_date = datetime.now()
start_date = datetime(2018, 1, 1)

for _ in range(500000):
    date = faker.date_time_between(start_date, end_date)
    client_id = randint(1, 1000000)
    print(f'{date}, {client_id}')