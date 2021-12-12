# 1. 모험가 길드
# 여행을 떠날 수 있는 그룹 수의 최댓값

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)
