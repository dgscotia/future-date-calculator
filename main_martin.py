# Script to figure out what date I will have spent half my life in Europe.

import datetime as dt
import re

pattern = '[0-9]{4}[/][0-9]{2}[/][0-9]{2}'


def run():
    birthday = get_birthday()
    change_date = get_change_date()
    calc_half_date(birthday, change_date)


def query_date(prefix_printed_on_screen):
    while True:
        user_input = input(prefix_printed_on_screen)
        if not re.match(pattern, user_input):
            print('Just follow the "YYYY/MM/DD" pattern, punk.\n')
            continue
        day, month, year = user_input.split("/")
        try:
            dt.datetime(int(year), int(month), int(day))
        except ValueError:
            print("That date doesn't exist.\n")
            continue
        return dt.date(int(year, month, day))


def get_birthday():
    return query_date('When were you born? (YYYY/MM/DD) ')


def get_change_date():
    return query_date('When did the thing start happening? (YYYY/MM/DD) ')


def calc_half_date(first_date, second_date):
    assert first_date < second_date
    delta = second_date - first_date
    final_date = second_date + delta
    if final_date > date.today():
        age = (final_date - first_date).days // 365
        print(f'You will have spent half your life doing this thing on {final_date}. You will be {age} years old.')

    else:
        print(f'You have already passed the halfway mark for this. It was {final_date}.')


if __name__ == '__main__':
    run()
