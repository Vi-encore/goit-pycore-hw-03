from datetime import datetime
from random import randint

# task 1

def get_days_from_today(date=None):
  if date is None:
    return 'You did not enter any date'
  try:
    given_date = datetime.strptime(date, '%Y-%m-%d').date()
    date_now = datetime.today()
    return given_date.toordinal() - date_now.toordinal()
  except (ValueError, TypeError):
    return 'Date should be in this format : YYYY-MM-DD'
  

# print(get_days_from_today('2025-03-01'))
# print(get_days_from_today('df'))
# print(get_days_from_today(23))
# print(get_days_from_today(True))
# print(get_days_from_today('2025-02-30'))
# print(get_days_from_today())

# task 2

def get_numbers_ticket(min=None, max=None, quantity=None):
  if min is None or max is None or quantity is None:
    return 'You should pass min,max and quantity for this function to work'
  
  try:
    if  1 <= min < max and min < max <= 1000 and 1 <= quantity <= 1000:
      result = set()
      while len(result) != quantity:
        result.add(randint(min, max))
      return sorted(list(result))
    else: 
      return 'Min should be greater or equal to 1\nMax should be lesser or equal to 1000\nQuantity should be between min and max'
  except (ValueError, TypeError):
    return 'You did not provide correct type of value'

# print(get_numbers_ticket())
# print(get_numbers_ticket(2,36,7)) #correct
# print(get_numbers_ticket('1','1000','3'))
# print(get_numbers_ticket('1',1000,'3'))
# print(get_numbers_ticket(1001,1000,3)) 
# print(get_numbers_ticket(1,1,3)) 
# print(get_numbers_ticket(True, '1000', 32))
# print(get_numbers_ticket(1, 32, True))
# print(get_numbers_ticket([], [],[]))
