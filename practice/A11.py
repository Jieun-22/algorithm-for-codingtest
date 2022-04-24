# 11 뱀

n = int(input())
data = [[0]*(n+1) for _ in range(n+1)]

k = int(input())
for _ in range(k):
  x, y = map(int, input().split())
  data[x][y] = 1

l = int(input())
info = [0] * (10001)

for _ in range(l):
  x, c = input().split()
  info[int(x)] = c

dx = [0, 1, 0, -1]
dy = [1,0,-1,0]

def turn_direction(direction, c):
  if c == 'L':
    direction = (direction-1)%4
  else:
    direction = (direction+1) % 4
  
  return direction

x,y = 1,1
data[x][y]  = 2
q = [(x,y)]
t = 0
direction = 0

while True:
  nx = x + dx[direction]
  ny = y + dy[direction]

  if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2 :
    if data[nx][ny] == 0: # 아무것도 없다면 
      data[nx][ny] = 2
      q.append((nx,ny))
      rx, ry = q.pop(0)
      data[rx][ry] = 0
    elif data[nx][nx] == 1 : #사과 있다면
      data[nx][ny] = 2
      q.apped((nx,ny))
  else:
    t += 1
    break
  x,y = nx, ny
  t += 1
  if info[t] != 0:
    direction = turn_direction(direction, info[t])

print(t)
