# 행성 터널

n = int(input())

data = []

for _ in range(n):
  x,y,z = map(int, input().split())
  data.append((x,y,z))

edges = []

for i in range(n):
  for j in range(i+1,n):
    cost = min(abs(data[i][0]- data[j][0]), abs(data[i][1]- data[j][1]), abs(data[i][2]- data[j][2]))
    edges.append((cost,i,j))

edges.sort()
parent = [0]*n

for i in range(n):
  parent[i] = i

result = 0

for edge in edges:
  cost,i,j = edge
  if find_parent(parent,i) != find_parent(parent,j):
    union_parent(parent,i,j)
    result += cost
  
print(result)
