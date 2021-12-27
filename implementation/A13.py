# 치킨배달

from itertools import combinations

n, m = map(int, input().split())
data = []
for i in range(n):
  data.append(list(map(int, input().split())))

chicken = []
house = []

for i in range(n):
  for j in range(n):
    if data[i][j] == 1:
      house.append([i,j])
    elif data[i][j] == 2:
      chicken.append([i,j])

candidates = list(combinations(chicken, m))
#조합 순서를 고려하지 않고 m개 뽑는 경우 list로 반환

def get_sum(candidate):
  result = 0 
  for hx, hy in house:
    temp = 1e9
    for cx, cy in candidate:
      temp = min(temp, abs(hx-cx) + abs(hy-cy))
    result += temp
  return result

result = 1e9
for candidate in candidates :
  result = min(result, get_sum(candidate))

print(result)
