# 볼링공 고르기

n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0

for i in range(len(data)):
  for j in range(i, len(data)):
    if data[i] != data[j] :
      count+= 1

print(count)

#---------------------------------------------------------
#

n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
  array[x] += 1

result = 0 

for i in range(1, m+1):
  n -= array[i]
  result += array[i]*n

print(result )
