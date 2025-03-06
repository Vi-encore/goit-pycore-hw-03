import re

#task 3

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
    

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
#     "37050-111-22-22",
#     'dggdf',
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
