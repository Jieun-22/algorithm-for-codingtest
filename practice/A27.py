#정렬된 배열에서 특정수의 개수 구하기

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))

first = bisect_left(data, x)
last = bisect_right(data, x)

result = last - first

if result == 0:
  print(-1)
else:
  print(result)


