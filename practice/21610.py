# 마법사 상어와 비바라기 21610

n, m = map(int, input().split())
array = [] #그래프
moves = [] # 이동
clouds = [] #구름 좌표

for _ in range(n):
  array.append(list(map(int, input().split())))

for _ in range(m):
  moves.append(list(map(int, input().split())))

clouds = [[n-1,0],[n-1,1],[n-2,0],[n-2,1]]

# 이동 방향 1~8
dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1] 

# 대각선 확인
x_x = [-1,-1,1,1]
x_y = [-1,1,1,-1]

def water_copy(x,y):
  cnt = 0

  for i in range(4):
    nx = x + x_x[i]
    ny = y + x_y[i]
    if nx >=0 and nx<n and ny >= 0 and ny <n:
      if array[nx][ny] > 0:
        cnt += 1
  return cnt

def cloud_make():
  new_clouds = []
  for i in range(n):
    for j in range(n):
      if array[i][j] >=2 :
        if [i,j] not in clouds:
          new_clouds.append([i,j])
          array[i][j] -= 2

  return new_clouds

for move in moves:
  d, s = move
  for i in range(len(clouds)):
    x,y = clouds[i][0], clouds[i][1]
    nx = (x + dx[d]*s) % n
    ny = (y + dy[d]*s) % n
    clouds[i] = [nx,ny]
  
  for x,y in clouds: #바구니 물 1 증가
    array[x][y] += 1
  
  for x,y in clouds: # 물 복사 버그
    array[x][y] += water_copy(x,y)

  clouds = cloud_make()

result = 0

for i in range(n):
  for j in range(n):
    result += array[i][j]

print(result)


