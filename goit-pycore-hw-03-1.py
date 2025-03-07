from datetime import datetime

#task 1

def get_days_from_today(date=None):
  if date is None:
    return 'You did not enter any date'
  try:
    given_date = datetime.strptime(date, '%Y-%m-%d').date()
    date_now = datetime.today().date() #work without date() as well
    return given_date.toordinal() - date_now.toordinal()
  except (ValueError, TypeError):
    return 'Date should be in this format : YYYY-MM-DD'
  


# print(get_days_from_today('2025-03-03'))
# print(get_days_from_today('df'))
# print(get_days_from_today(23))
# print(get_days_from_today(True))
# print(get_days_from_today('2025-02-30'))
# print(get_days_from_today())