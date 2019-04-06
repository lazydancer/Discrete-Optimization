from collections import namedtuple
import copy

def calc_weight(path_stack, items):
  total = 0
  for (i, p) in enumerate(path_stack):
    if p == 1:
      total += items[i].weight

  return total

def calc_value(path_stack, items, capacity):
  if calc_weight(path_stack, items) > capacity:
    return 0

  total = 0
  for (i, p) in enumerate(path_stack):
    if p == 1:
      total += items[i].value

  return total

def estimated_value(path_stack, items, capacity):
  
  curr_value = calc_value(path_stack, items, capacity)
  remaining_capacity = capacity - calc_weight(path_stack, items) 

  remaining_items = copy.copy(items[len(path_stack):])
  remaining_items.sort(key=lambda x: x.value/x.weight, reverse=True)

  rest = 0
  for i in remaining_items:
    if i.weight < remaining_capacity:
      rest += i.value
      remaining_capacity -= i.weight
    else:
      rest += ((i.value / i.weight) * remaining_capacity)
      break

  return curr_value + rest 

def isStop(path_stack, items, capacity, max_value):
  if calc_weight(path_stack, items) > capacity:
    return True
  
  value = estimated_value(path_stack, items, capacity)
  #print(path_stack, value, max_value)
  if value < max_value:
    return True

  return False


def get_next(path_stack, length, up):
  # Gets next item to check
  up_from = None
  if up:
    up_from = path_stack.pop()

  if len(path_stack) == length:
    return get_next(path_stack, length, True)

  elif up_from == 0:
    if path_stack == []:
      return path_stack
    return get_next(path_stack, length, True)

  elif up_from == 1:
    path_stack.append(0)
    return path_stack

  elif up_from == None:
    path_stack.append(1)
    return path_stack

  print("You shouldnt be here in get_next")

''' get_next tests
  print(get_next([], 5, False), [1])
  print(get_next([1,1,1,1,1], 5, False), [1,1,1,1,0])
  print(get_next([1,1,1,0,0], 5, False), [1,1,0])
  print(get_next([0,0,0,0,1], 5, False), [0,0,0,0,0])
  print(get_next([0,0,0,0,0], 5, False), [])
  print(get_next([1,0,0,0,0], 5, False), [0])
'''

def generateHash(items):

  items_hash = dict()
  for x in items:
    items_hash[x.index] = x

  return items_hash


def run(items, capacity):

  max_input = []
  max_value = 0

  path_stack = []

  length = len(items)
  up = False

  MAX_ITER = 9999999
  i = 0
  while i < MAX_ITER:
    i += 1
    if i % 10000 == 0:
      print(i)
    
    path_stack = get_next(path_stack, length, up)
    
    if path_stack == []:
      break;

    up = isStop(path_stack, items, capacity, max_value)

    if not up:
      value = calc_value(path_stack, items, capacity)
      if value > max_value:
        max_value = value
        max_input = copy.copy(path_stack)

  diff =  len(items) - len(max_input)
  for _ in range(diff):
    max_input.append(0)

  max_reached = 0
  if i < MAX_ITER:
    max_reached = 1

  return (max_input, max_value, max_reached)