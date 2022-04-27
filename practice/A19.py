# 연산자 끼워 넣기
from itertools import permutations

n = int(input())
data = list(map(int, input().split()))
array = list(map(int, input().split()))

oper = []

for i in range(4):
  for j in range(array[i]):
    oper.append(i)

candidates = list(permutations(oper,n-1))

min_value = int(1e9)
max_value = 0

for c in candidates:
  result = data[0]
  for i in range(1,n):
    if c[i-1] == 0:
      result += data[i]
    elif c[i-1] == 1:
      result -= data[i]
    elif c[i-1] == 2:
      result *= data[i]
    elif c[i-1] == 3:
      result = int(result/data[i])
  min_value = min(min_value, result)
  max_value = max(max_value, result)

print(max_value)
print(min_value)
