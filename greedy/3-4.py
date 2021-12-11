# 1이 될때까지 -1 , /k 연산의 최소 횟수 구하기

n, k = map(int, input().split())
result = 0

while True:
  target = (n//k) *k
  result += (n-target)
  n = target
  if n<k:
    break
  n //= k
  result += 1

result += (n-1)
print(result)
