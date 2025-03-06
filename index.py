from datetime import datetime,timedelta
from random import randint
import re

#previous commit is with some makeshift tests (just print(), without assert)

# task 1

def get_days_from_today(date=None):
  if date is None:
    return 'You did not enter any date'
  try:
    given_date = datetime.strptime(date, '%Y-%m-%d').date()
    date_now = datetime.today().date() #work without date() as well
    return given_date.toordinal() - date_now.toordinal()
  except (ValueError, TypeError):
    return 'Date should be in this format : YYYY-MM-DD'
  

# task 2

def get_numbers_ticket(min=None, max=None, quantity=None):
  if min is None or max is None or quantity is None:
    return []
  
  for arg in (min, max, quantity):  #to throw away bools
    if isinstance(arg, bool):
      return []

  try:
    if  1 <= min < max and min < max <= 1000 and 1 <= quantity <= 1000:
      result = set()
      while len(result) != quantity:
        result.add(randint(min, max))
      return sorted(list(result))
    else: 
      return []
  except (ValueError, TypeError) as error:
    print(error) #do I need to print error? 
    return []

#task 3

#delete test list

def normalize_phone(num: str):
  pattern = r'[^+\d]'
  clean_phone = re.sub(pattern, '', num)

  match clean_phone:
    case _ if re.match(r'^\+380\d{9}$', clean_phone):
      return clean_phone
    case _ if re.match(r'^380\d{9}$', clean_phone):
      return f'+{clean_phone}'
    case _ if re.match(r'^0\d{9}$', clean_phone):
      return f'+38{clean_phone}'
    case _:
      return 'Phone format is invalid'


#task 4

def get_upcoming_birthdays(users: list):
  day_today = datetime.today().date()
  upcoming_birthdays = []

  for user in users:
    birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date() # this var here - so next var is more readable 
    birthday_this_year = birthday_date.replace(year=day_today.year)


    if birthday_this_year < day_today:
      birthday_this_year = birthday_this_year.replace(year=day_today.year+1)

    if 0 <= (birthday_this_year - day_today).days <= 7:
      congrats_day = birthday_this_year;

      if birthday_this_year.weekday() in {5,6}:
        congrats_day += timedelta(days=(7-congrats_day.weekday()))

      upcoming_birthdays.append({
        'name': user['name'],
        'congratulation_date': congrats_day.strftime("%Y-%m-%d")
      })
  return upcoming_birthdays
