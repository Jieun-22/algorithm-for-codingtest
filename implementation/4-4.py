# 게임개발

n, m = map(int, input().split())
x, y, d = map(int, input().split())

data = []
for i in range(n):
  data.append(list(map(int, input().split())))

map = [[0]*m for _ in range(n)]
map[x][y] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
  global d
  d -= 1
  if d < 0 :
    d = 3

count = 1
turn_time = 0

while True:
  turn_left()

  nx = x + dx[d]
  ny = y + dy[d]

  if map[nx][ny] == 0 and data[nx][ny] == 0:
    map[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  
  else:
    turn_time += 1
  
  if turn_time == 4: #네 방향 모두 갈 수 없는 경우
    nx = x - dx[d]
    ny = y - dy[d]
    if data[nx][ny] == 0: 
      x = nx
      y = ny
      turn_time = 0
    else: # 뒤가 바다인 경우
      break

print(count)
      



