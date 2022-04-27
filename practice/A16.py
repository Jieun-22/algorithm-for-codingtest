# 연구소
from itertools import combinations
import copy

n, m = map(int, input().split())

graph = []
virus = []
blank = []

for i in range(n):
  data = list(map(int, input().split()))
  graph.append(data)
  for j in range(m):
    if data[j] == 0:
      blank.append((i,j))
    elif data[j] == 2:
      virus.append((i,j))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(graph,x,y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx <n and ny >= 0 and ny <m:
      if graph[nx][ny] ==0:
        graph[nx][ny] = 2
        dfs(graph,nx,ny)

def count(graph):
  n = len(graph)
  m = len(graph[0])
  count = 0

  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        count += 1
  return count

candidates = list(combinations(blank, 3))
temp = copy.deepcopy(graph)
result = 0

for candidate in candidates:
  for x,y in candidate:
    temp[x][y] = 1
  for v in virus:
    dfs(temp,v[0],v[1])
  result = max(result, count(temp))
  temp = copy.deepcopy(graph)

print(result)
