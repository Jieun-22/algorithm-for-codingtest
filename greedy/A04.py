# 만들 수 없는 금액

n = int(input())
data = list(map(int, input().split()))

data.sort()

num = 1 # 1 부터 num-1 까지 만들 수 있음 
for i in data:
  if num < i :
    break
  num += i

print(num)
