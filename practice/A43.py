# 어두운 길

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

n, m = map(int, input().split())
edges = []
parent = [0]*(n)

for i in range(1,n):
  parent[i] = i

sum = 0

for _ in range(m):
  x, y, cost = map(int, input().split())
  edges.append((cost,x,y)) 
  sum += cost

edges.sort()

remain_cost = 0

for edge in edges:
  cost,x,y = edge
  if find_parent(parent,x) != find_parent(parent,y):
    union_parent(parent,x,y)
    remain_cost += cost

print(sum-remain_cost)
  

