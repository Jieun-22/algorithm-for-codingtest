# 숨바꼭질

import heapq

INF = int(1e9)

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append((b,1))
  graph[b].append((a,1))

q = []
heapq.heappush(q,(0,1))
distance[1] = 0
while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist :
    continue
  for i in graph[now]:
    cost = dist + i[1]
    if cost < distance[i[0]]:
      distance[i[0]] = cost
      heapq.heappush(q,(cost, i[0]))

num = 0
max_cost = 0
count = 0

for i in range(2,n+1):
  if distance[i] == INF:
    continue
  if distance[i] > max_cost :
    num = i
    max_cost = distance[i]
    count = 1
  elif distance[i] == max_cost :
    count += 1


print(num, max_cost, count)


