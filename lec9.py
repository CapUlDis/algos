from re import M


def merge(A: list, B: list):
  C = [0] * (len(A) + len(B))
  i = k = n = 0
  while i < len(A) and k < len(B):
    if A[i] <= B[k]:
      C[n] = A[i]
      i += 1
      n += 1
    else:
      C[n] = B[k]
      k += 1
      n += 1
  
  while i < len(A):
    C[n] = A[i]
    i += 1
    n += 1

  while k < len(B):
    C[n] = B[k]
    k += 1
    n += 1

  return C

def merge_sort(A):
  # начнём с крайнего случая
  if len(A) <= 1:
    return

  middle = len(A) // 2

  L = [A[i] for i in range(0, middle)]
  R = [A[i] for i in range(middle, len(A))]

  merge_sort(L)
  merge_sort(R)
  
  C = merge(L, R)
  for i in range(len(A)):
    A[i] = C[i]

G = [7, 5, 8, 3, 9, 11, 22, 3, 4, 5]
# merge_sort(G)

# print(*G)

def hoar_sort(A):
  if len(A) <= 1:
    return

  barrier = A[0]
  L = []
  M = []
  R = []
  for x in A:
    if x < barrier:
      L.append(x)
    elif x == barrier:
      M.append(x)
    else:
      R.append(x)

  hoar_sort(L)
  hoar_sort(R)

  k = 0
  for x in L + M + R:
    A[k] = x
    k += 1

hoar_sort(G)
# print(*G)

def check_sorted(A, ascending=True):
  """Проверка отсортированности за O(len(A))"""

  flag = True
  s = 2 * int(ascending) - 1
  for i in range(0, len(A) - 1):
    if s * A[i] > s * A[i + 1]:
      flag = False
      break
  
  return flag

print(check_sorted(G))
