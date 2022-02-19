# Script to figure out what date I will have spent half my life in Europe.

from datetime import date, timedelta
import re
birthday = ''
change_date = ''

# INPUT METHOD
while birthday == '':
    bday_input = input("When were you born? (YYYY/MM/DD) ")
    if not re.match("[0-9]{4}[/][0-9]{2}[/][0-9]{2}", bday_input):
        continue
    birthday = date(int(bday_input.split("/")[0]), int(bday_input.split("/")[1]), int(bday_input.split("/")[2]))
    # Q for Martin - is there a slick way to do one-line comprehension so I can feed the list into the datetime object
    # without having to manually put in the list indices? I tried it on the line below but couldn't get it to work.
    # birthday = date(int(i) for i in bday_list)

while change_date == '':
    change_input = input("When did the thing start happening? (YYYY/MM/DD) ")
    if not re.match("[0-9]{4}[/][0-9]{2}[/][0-9]{2}", change_input):
        continue
    change_date = date(int(change_input.split("/")[0]), int(change_input.split("/")[1]), int(change_input.split("/")[2]))
    # Same Q for Martin as above!

# SHORTCUT METHOD
# birthday = date(1988,8,3)
# change_date = date(2012,10,15)

half_date = date.today()

if half_date - change_date >= change_date - birthday:
    while half_date - change_date >= change_date - birthday:
        half_date -= timedelta(days=1)

    final_date = half_date.strftime("%d %B %Y")

    print("\nYou've already passed the halfway mark for this.")
    print(f"It was {final_date}.")

else:
    # Q for Martin - is there a simpler way to calculate half_date besides incrementing it?
    while half_date - change_date <= change_date - birthday:
        half_date += timedelta(days=1)

    final_date = half_date.strftime("%d %B %Y")
    age = round((half_date - birthday).days/365)

    print(f"\nYou will have spent half your life doing this thing on {final_date}.")
    print(f"You will be {age} years old.")
