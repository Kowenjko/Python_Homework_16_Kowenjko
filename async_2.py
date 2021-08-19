import csv
from faker import Faker
import tracemalloc
import time
import asyncio
import base

fake = Faker()


async def write_csv(address, mode, dictionary):
    file = open(address, mode, encoding='UTF-8', newline='')
    writer = csv.writer(file)
    writer.writerow(dictionary)
    file.close()


async def create_person(count):
    person = []
    tasks = []
    person.append(count)
    person.append('->')
    person.append(fake.first_name())
    person.append(fake.last_name())
    person.append(fake.user_name())
    person.append(fake.password())
    person.append(fake.street_address())
    task = asyncio.ensure_future(write_csv('data.csv', 'a', person))
    tasks.append(task)
    responses = await asyncio.gather(*tasks)
    return responses


if __name__ == "__main__":

    tracemalloc.start()
    start = time.time()

    program = ["Mode - async-2"]
    base.write_csv('data.csv', 'w', program)

    for i in range(0, base.copy):
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(create_person(i+1))
        loop.run_until_complete(future)
        responses = future.result()

    base.print_txt('Async 2', start)

    print('Async 2')
    print("Curent %d, Peak %d" % tracemalloc.get_traced_memory())
    print("All done! {}".format(time.time() - start))
