def left_bound(A, key):
  left = -1
  right = len(A)
  while right - left > 1:
    middle = (left + right) // 2
    if A[middle] < key:
      left = middle
    else:
      right = middle
  
  return left

def right_bound(A, key):
  left = -1
  right = len(A)
  while right - left > 1:
    middle = (left + right) // 2
    if A[middle] <= key:
      left = middle
    else:
      right = middle
  
  return right


def fib(n):
  if n <= 1:
    return n
  
  return (fib(n - 1) + fib(n - 2))

def fib_alg(n):
  fib = [0, 1] + [0] * (n - 1)
  for i in range(2, n + 1):
    fib[i] = fib[i - 1] + fib[i - 2 ]

  return fib[n]

# print(fib_alg(11))

def traj_num(n):
  K = [0, 1] + [0] * n
  for i in range(2, n + 1):
    K[i] = K[i - 2] + K[i - 1]
  
  return K(n)

def count_trajectories(N, allowed: list):
  K = [0, 1, int(allowed[2])] + [0] * (N - 3)
  print(K)
  for i in range(3, N):
    if allowed[i]:
      K[i] = K[i - 1] + K[i - 2] + K[i - 3]

  return K[N - 1]

# print(count_trajectories(9, [True, True, False, False, True, True, False, True, True]))

def count_min_cost(N, price: list):
  C = [0, price[1], min(price[1], price[2])] + [0] * (N - 2)
  for i in range(3, N + 1):
    # print((C[i - 1], C[i - 2]))
    C[i] = price[i] + min(C[i - 1], C[i - 2])

  print(C)
  return C[N]

# print(count_min_cost(3, [0, 3, 1, 5, 3, 7, 4, 5, 1]))

print([([0] * 4) for i in range(5)])