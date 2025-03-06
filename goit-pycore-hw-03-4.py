from datetime import datetime, timedelta

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


# users = [
#     {"name": "John Doe", "birthday": "1985.01.23"},
#     {"name": "Jane Smith", "birthday": "1990.01.27"},
#     {"name": "Jane Smith", "birthday": "1990.03.09"}

# ]


# upcoming_birthdays = get_upcoming_birthdays(users)
# print("Список привітань на цьому тижні:", upcoming_birthdays)