# 13 치킨 배달
from itertools import combinations

n, m = map(int, input().split())

home = []
chicken = []

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] == 1:
      home.append((i,j))
    elif data[j] == 2:
      chicken.append((i,j))

candidates = list(combinations(chicken, m))

result = 999999999

for candidate in candidates:
  sum = 0
  for h in home :
    x = 999999999
    for c in candidate:
      distance = abs(h[0] - c[0]) + abs(h[1] - c[1])
      x = min(x, distance)
    sum += x
  result = min(result, sum)

print(result)
   


