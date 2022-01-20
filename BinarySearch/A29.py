n, c = map(int, input().split())
array = []

for i in range(n):
  array.append(int(input()))

array.sort()

start = 1 #min gap
end = array[-1] - array[0] # 가능한 최대 거리
result = 0

while(start <= end):
  mid = (start+end)//2 # 가장 인접한 두 공유기 사이의 거리
  value = array[0]
  count = 1
  for i in range(1,n):
    if array[i] >= value + mid:
      value = array[i]
      count += 1
    if count >= c:
      start = mid+1
      result = mid
    else:
      end = mid-1

print(result)
