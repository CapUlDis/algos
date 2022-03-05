def generate_numbers(N: int, M: int, prefix = None):
  """Генерирует все числа (с лидирующими незначащами нулями)
  в N-ричной системе счисления (N <= 10) длины M"""
  if M == 0:
    print(prefix)
    return
  prefix = prefix or []
  for digit in range(N):
    prefix.append(digit)
    generate_numbers(N, M - 1, prefix)
    prefix.pop()

def gen_bin(M, prefix = ""): #только для двоичной системы счисления
  if M == 0:
    print(prefix)
    return
  for digit in "0", "1":
    gen_bin(M - 1, prefix + digit)
    
# gen_bin(3)

# generate_numbers(3, 3)

def find(number, A):
  flag = False
  for x in A:
    if number == x:
      flag = True
      break
  return flag
    

def generate_permutations(N: int, M: int = -1, prefix = None):
  """Генерация всех перестановок N чисел в M позициях
  с префиксом prefix"""
  M = M if M != -1 else N  # по умолчанию N чисел в N позициях
  prefix = prefix or []
  if M == 0:
    print(*prefix)
    return
  for number in range(1, N + 1):
    if find(number, prefix):
      continue
    prefix.append(number)
    generate_permutations(N, M - 1, prefix)
    prefix.pop()

generate_permutations(4)