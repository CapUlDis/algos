def is_simple_number(x):
  """Определяет является ли число простым
  """
  divisor = 2
  while divisor < x:
    if x%divisor == 0:
      return False
    divisor += 1
  return True

print(help(is_simple_number))