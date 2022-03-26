#럭키 스트레이트 A07

data = input()
mid = int(len(data)/2)

left = 0
right = 0

for i in range(0,mid):
  left += int(data[i])

for i in range(mid,len(data)):
  right += int(data[i])

if left == right :
  print('LUCKY')
else:
  print('READY')
