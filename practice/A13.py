# 치킨배달

from itertools import combinations

n, m = map(int, input().split())

home = []
chicken = []

for x in range(n):
  data = list(map(int, input().split()))
  for y in range(n):
    if data[y] == 1:
      home.append((x,y))
    elif data[y] == 2:
      chicken.append((x,y))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
  result = 0
  for hx, hy in home:
    temp = 1e9
    for cx,cy in candidate:
      temp = min(temp, abs(hx-cx) + abs(hy-cy))

    result += temp
  return result

result = 1e9
for candidate in candidates:
  result = min(result, get_sum(candidate))

print(result)

