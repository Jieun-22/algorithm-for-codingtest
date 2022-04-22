# 행성 터널
from itertools import combinations

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])

  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a <b:
    parent[b] = a
  else:
    parent[a] = b

n = int(input())
loc = []

for _ in range(n):
  loc.append(list(map(int, input().split())))

array = [i for i in range(n)]

candidates = list(combinations(array,2))

edges = []
parent = [0]*(n)

for i in range(n):
  parent[i] = i

for candidate in candidates:
  a,b = candidate
  cost = min(abs(loc[a][0]-loc[b][0]), abs(loc[a][1]-loc[b][1]), abs(loc[a][2]- loc[b][2]))
  edges.append((cost,a,b))

edges.sort()

result = 0

for edge in edges:
  cost, a, b = edge
  if find_parent(parent,a) != find_parent(parent,b):
    union_parent(parent,a,b)
    result += cost
  
print(result)
