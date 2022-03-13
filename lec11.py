def largest_common_subsequence(A, B):
  # зарезривируем память для вычислений, на 1 больше длины, чтобы включить нулевой столбец
  F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
  for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
      if A[i - 1] == B[j - 1]:
        F[i][j] = 1 + F[i - 1][j - 1]
      else:
        F[i][j] = max(F[i - 1][j], F[i][j - 1])
  
  return F[-1][-1]

A = [1, 2, 5, 4, 8, 6, 7, 4, 8, 8, 9, 3]
B = [3, 4, 6, 5, 7, 8, 8, 4, 5, 9, 3, 4, 6, 7, 8, 9]
C = [1, 4, 5, 9, 3]
D = [2, 4, 7, 9, 3]

G= [6, 5, 3, 2, 1]

# print(largest_common_subsequence(C, D))

def greatest_incresing_subsequence(A):
  F = [0] * len(A)
  for i in range(len(A)):
    for j in range(i):
      if A[i] < A[j] and F[j] > F[i]:
        F[i] = F[j]
    F[i] += 1
  
  print(F)
  return max(*F)

print(greatest_incresing_subsequence(A))