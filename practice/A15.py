# 특정 거리의 도시 찾기 A15
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

INF = 999999999

distance = [INF]*(n+1)

def bfs(graph, start):
  queue = deque([start])
  distance[start] = 0 
  
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      distance[i] = min(distance[i], distance[v]+1)
      queue.append(i)

bfs(graph, x)

result = []

check = False

for i in range(1, n+1):
  if distance[i] == k:
    print(i)
    check = True

if check == False:
  print(-1)
