# 인구이동

from collections import deque

n, l, r = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x,y, index):
  # 연결된 나라 정보 담는 리스트
  united = []
  united.append((x,y))

  q = deque()
  q.append((x,y))
  union[x][y] = index # 현재 연합의 번호 할당
  summary = graph[x][y]
  count = 1

  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0<= ny <n and union[nx][ny] == -1:
        # 인구수 확인
        if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
          q.append((nx,ny))
          union[nx][ny] = index
          summary += graph[nx][ny]
          count += 1
          united.append((nx,ny))
  
  for i,j in united:
    graph[i][j] = summary // count 
  
  return count

total_count = 0

while True:
  union = [[-1] *n for _ in range(n)]
  index = 0
  for i in range(n):
    for j in range(n):
      if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
        process(i,j, index)
        index += 1
  print(union)
  if index == n*n :
    break
  total_count += 1

print(total_count)
