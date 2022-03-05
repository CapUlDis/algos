# def matryoshka(n):
#   if n == 1:
#     print("Матрёшечка")
#   else:
#     print("Верх матрёшки n=", n)
#     matryoshka(n - 1)
#     print("Низ матрёшки n=", n)

# matryoshka(5)

def f(n: int):
  assert n >= 0, "Факториал отрицательных не определён"
  if n == 0:
    return 1
  return f(n - 1) * n

def gcd(a, b):
  if a == b:
    return a
  elif a > b:
    return gcd(a - b, b)
  else: # a < b
    return gcd(a, b - a)

def gcd2(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

def gcd3(a, b):
  return a if b == 0 else gcd(b, a % b)

def pow(a: float, n: int):
  if n == 0:
    return 1
  else:
    return pow(a, n - 1) * a

def pow2(a: float, n: int):
  if n == 0:
    return 1
  elif n % 2 == 1: #  нечётные
    return pow(a, n - 1) * a
  else: # чётные
    return pow(a ** 2, n // 2)

print(pow2(2, 4))