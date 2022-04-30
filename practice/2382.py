# 2382 미생물 격리


t = int(input())

dx = ['',-1,1,0,0]
dy = ['',0,0,-1,1]
rev = ['',2,1,4,3]
array = []
cluster = []

n,m,k = 0,0,0

def move_cluster():
  new_array = [[[]for _ in range(n)] for _ in range(n)]

  for i in range(k):
    if cluster[i] == 0:
      continue
    x,y,s,d = cluster[i]
    nx = x + dx[d]
    ny = y + dy[d]
    if nx == 0 or nx == n-1 or ny == 0 or ny == -1: # 끝에 닿으면
      new_s = int(s/2)
      new_d = rev[d]
      if new_s == 0:
        cluster[i] = 0
        continue
      else:
        new_array[nx][ny].append(i)
        cluster[i] = [nx,ny,new_s, new_d]
    else:
      new_array[nx][ny].append(i)
      cluster[i] = [nx,ny,s,d]

  return new_array

def sum_cluster(a,b):
  d_index = -1 # 미생물 수 가장 많은 군집 번호
  new_d = 0
  max_size = 0 # 미생물 수
  new_s = 0

  for i in array[a][b]:
    if cluster[i] == 0:
      continue
    x,y,s,d = cluster[i]
    if d > max_size:
      d_index = i
      max_size = s
      new_d = d
    else: cluster[i] = 0
    new_s += s

  array[a][b]= [d_index]
  cluster[d_index] = (a,b,new_s, new_d)


for tc in range(1,t+1):
  n, m, k = map(int, input().split())

  array = [[[]for _ in range(n)] for _ in range(n)]
  cluster = [0]*k #미생물 번호 index 로 x,y,size, direction 조회

  result = 0

  for i in range(k):
    x,y,s,d = map(int,input().split())
    cluster[i] = [x,y,s,d]
    array[x][y].append(i)

  for _ in range(m):
    array = move_cluster()

    for i in range(n):
      for j in range(n):
        if len(array[i][j]) >1 :
          sum_cluster(i,j)

  for i in range(k):
    data = cluster[i]

    if data != 0:
      result += data[2]

  print('#{0} {1}'.format(tc, result))
