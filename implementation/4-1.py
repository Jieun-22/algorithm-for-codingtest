# 상하좌우

n = int(input())
data = input().split()

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for move in data:
  for i in range(4):
    if move == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx <1 or ny <1 or nx>n or ny>n :
    continue
  x, y = nx, ny


print(x, y)
