from random import randint, sample

# task 2

def get_numbers_ticket(min=None, max=None, quantity=None):
  if min is None or max is None or quantity is None:
    return []
  
  for arg in (min, max, quantity):  #to throw away bools
    if isinstance(arg, bool):
      return []

  try:
    if  1 <= min < max and min < max <= 1000 and min <= quantity <= max: #oops, my bad. changed to min/max values
      # result = set()
      # while len(result) != quantity:
      #   result.add(randint(min, max))
      # # return sorted(list(result))

      return sorted(sample(range(min, max), quantity)) #other way of solving
    
    else: 
      return []
  except (ValueError, TypeError) as error:
    print(error) #do I need to print an error? 
    return []


# print(get_numbers_ticket())
# print(get_numbers_ticket(2,36,3)) #correct
# print(get_numbers_ticket('1','1000','3'))
# print(get_numbers_ticket('1',1000,'3'))
# print(get_numbers_ticket(1001,1000,3)) 
# print(get_numbers_ticket(1,1,3)) 
# print(get_numbers_ticket(True, '1000', 32))
# print(get_numbers_ticket(1, 32, True)) 
# print(get_numbers_ticket([], [],[]))