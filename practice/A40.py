#40 숨바꼭질
import heapq

n, m = map(int, input().split())

INF = int(1e9)

graph= [[]for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a,b = map(int, input().split())
  graph[a].append((b,1))
  graph[b].append((a,1))

q= []
distance[1] = 0
heapq.heappush(q,(0,1))

while q:
  dist, now = heapq.heappop(q)
  if distance[now] < dist:
    continue
  for i in graph[now]:
    cost = dist + i[1]
    if cost < distance[i[0]]:
      distance[i[0]] = cost
      heapq.heappush(q,(cost, i[0]))

num = 0
dis = 0
cnt = 0

for i in range(1,n+1):
  if distance[i] == INF:
    continue
  if distance[i] > dis:
    num = i
    dis = distance[i]
    cnt = 1
  elif distance[i] == dis:
    cnt += 1

print(num, dis, cnt)



