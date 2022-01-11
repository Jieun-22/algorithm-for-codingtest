#감시 피하기

from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
  board.append(list(input().split()))
  for j in range(n):
    if board[i][j] == 'T':
      teachers.append((i,j))
    if board[i][j] == 'X':
      spaces.append((i,j))

def watch(x,y,direction):
  if direction == 0 : #왼쪽방향
    while y >= 0:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      y -= 1
  if direction == 1 : # 오른쪽방행
    while y < n:
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      y += 1
  if direction == 2: #위쪽방향
    while x >= 0 :
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      x -= 1
  if direction == 3 : # 아래쪽방향
    while x <n :
      if board[x][y] == 'S':
        return True
      if board[x][y] == 'O':
        return False
      x += 1
  return False

def process():
  for x, y in teachers :
    for i in range(4):
      if watch(x,y,i):
        return True
  return False

find = False

for data in combinations(spaces, 3):
  for x,y in data:
    board[x][y] = 'O'
  if not process():
    find = True
    break
  
  for x, y in data:
    board[x][y] = 'X'

if find:
  print('YES')
else:
  print('NO')
