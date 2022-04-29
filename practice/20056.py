#20056 마법사 상어와 파이어볼 

n, m, k = map(int, input().split())

array = [[[]for _ in range(n)] for _ in range(n)]

for _ in range(m):
  r,c,m,s,d = map(int, input().split())
  array[r-1][c-1].append([m,s,d])

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def move_balls():
  new_array = [[[] for _ in range(n)] for _ in range(n)]
  for x in range(n):
    for y in range(n):
      if len(array[x][y]) != 0 :
        for data in array[x][y]:
          m,s,d = data
          nx = (x + dx[d]*s)%n
          ny = (y + dy[d]*s)%n

          new_array[nx][ny].append([m,s,d])
        
  return new_array


def sum_mass():
  result = 0

  for i in range(n):
    for j in range(n):
      data = array[i][j]
      for k in range(len(data)):
        result += data[k][0]
  return result


def divide_balls(x,y):
  sum_m, sum_s, cnt, odd_cnt, even_cnt = 0,0,0,0,0

  for data in array[x][y]:
    m,s,d = data
    sum_m += m
    sum_s += s
    cnt += 1
    if (d%2) == 1:
      odd_cnt += 1
    else:
      even_cnt += 1

  array[x][y] = []

  if odd_cnt == cnt or even_cnt == cnt:
    direction = [0,2,4,6]
  else:
    direction = [1,3,5,7]

  
  for i in range(4):
    new_m = sum_m//5
    new_s = sum_s//cnt
    new_d = direction[i]
    if new_m != 0:
      array[x][y].append([new_m, new_s, new_d])
    
for _ in range(k):
  array = move_balls()
  for i in range(n):
    for j in range(n):
      if len(array[i][j])>1:
        divide_balls(i,j)
        
print(sum_mass())

        
