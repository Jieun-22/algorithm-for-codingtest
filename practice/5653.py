# 5653 줄기세포 배양 프로그램

t = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

n,m,k = map(int, input().split())

vessel = [[0]*800 for _ in range(800)]

array = []

for _ in range(n):
  array.append(list(map(int, input().split())))

act = []
deact = []

for i in range(n):
  for j in range(m):
    vessel[400+i][400+j] = array[i][j]
    deact.append((400+i,400+j,array[i][j]))

def cell(deact, vessel):
  c_act = []
  c_deact = []

  for x,y,v in deact:
    if v >= 1: # 활성화
      if v == 1:
        c_act.append((x,y,vessel[x][y]))
      else:
        c_deact.append((x,y,v-1))
    
  return c_act, c_deact
    
def propagation(act, vessel):
  p_act = []
  p_deact = []
  act.sort(reverse = True)

  for x, y, v in  act:
    if v >=1 :
      if v == vessel[x][y] : #  방금 활성화 됐으면
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if vessel[nx][ny] == 0:
            vessel[nx][ny] = vessel[x][y]
            p_deact.append((nx,ny,vessel[x][y]))
      if v > 1:
        p_act.append((x,y,v-1))
  
  return p_act, p_deact

def simulation(act, deact, vessel):
  p_act, p_deact = propagation(act,vessel)
  c_act, c_deact = cell(deact, vessel)

  return c_act+ p_act, c_deact + p_deact

for tc in range(1,t+1):
  for i in range(k):
    act, deact = simulation(act, deact, vessel)

  print(len(act) + len(deact))

  



