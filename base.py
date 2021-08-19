"""
Використовуючи різні підходи до мультизадачного програмування записати у csv файл 10 000 записів про людину,
використовуючи можливості бібліотеки faker(прізвище, ім'я, логін, пароль, адреса).

При кожному запуску програм файл повинен перезаписуватись.

"""


import csv
from faker import Faker
import tracemalloc
import time

copy = 10000

fake = Faker()


def write_txt(adress, dictionary):
    file = open(adress, 'a')
    file.write(dictionary)
    file.close()


def create_person(count):
    person = []
    person.append(count)
    person.append('->')
    person.append(fake.first_name())
    person.append(fake.last_name())
    person.append(fake.user_name())
    person.append(fake.password())
    person.append(fake.street_address())
    write_csv('data.csv', 'a', person)


def write_csv(address, mode, dictionary):
    file = open(address, mode, encoding='UTF-8', newline='')
    writer = csv.writer(file)
    writer.writerow(dictionary)
    file.close()


def print_txt(title, start):
    write_txt('result.txt', '\n')
    write_txt('result.txt', '-'*50)
    write_txt('result.txt', f'\n{title}\n')
    write_txt('result.txt', '-'*50)
    write_txt('result.txt', "\n\tCurent %d, Peak %d" %
              tracemalloc.get_traced_memory())
    write_txt('result.txt', f"\n\tAll done! {format(time.time()-start)}")
