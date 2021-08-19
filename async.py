import csv
from faker import Faker
import tracemalloc
import time
import asyncio
import base


async def create_person(count):
    person = []
    person.append(count)
    person.append('->')
    person.append(fake.first_name())
    person.append(fake.last_name())
    person.append(fake.user_name())
    person.append(fake.password())
    person.append(fake.street_address())
    base.write_csv('data.csv', 'a', person)


async def main():
    tasks = [asyncio.create_task(create_person(i+1))
             for i in range(0, base.copy)]
    await asyncio.gather(*tasks)

program = ["Mode - async"]
base.write_csv('data.csv', 'w', program)

fake = Faker()
tracemalloc.start()
start = time.time()

asyncio.run(main())

base.print_txt('Async', start)

print('Async')
print("Curent %d, Peak %d" % tracemalloc.get_traced_memory())
print(f"All done! {format(time.time()-start)}")
