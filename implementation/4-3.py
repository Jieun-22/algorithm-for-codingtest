# 왕실의 나이트

data = input()

x = ord(data[0]) - ord('a') +1
y = int(data[1])

move = [[-1,-2], [1,-2], [-2, -1], [-2,1], [2,-1], [2,1], [-1, 2], [1,2]]

count = 0

for plan in move:
  nx = x + plan[0]
  ny = y + plan[1]
  if nx<1 or ny<1 or nx>8 or ny>8:
    continue
  count += 1

print(count)
