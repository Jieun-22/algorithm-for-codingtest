# 39 화성 탐사
import heapq

INF = int(1e9)

t = int(input())

for _ in range(t):
  n = int(input())

  graph = []
  for _ in range(n):
    graph.append(list(map(int, input().split())))

  result= [[INF]*n for _ in range(n)]

  dx = [0,1,0,-1]
  dy = [1,0,-1,0]
  
  result[0][0] = graph[0][0]
  q = []
  heapq.heappush(q,(result[0][0],0,0))

  while q:
    dist, x, y = heapq.heappop(q)
    if result[x][y] < dist:
      continue
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >= 0 and nx <n and ny >= 0 and ny <n:
        cost = dist + graph[nx][ny]
        if cost < result[nx][ny]:
          result[nx][ny] = cost
          heapq.heappush(q,(cost, nx,ny))
          
  print(result[n-1][n-1])
  
