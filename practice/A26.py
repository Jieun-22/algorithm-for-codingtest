#카드 정렬하기

n = int(input())

data = []

for _ in range(n):
  data.append(int(input()))

data.sort()
result = []

summary = data[0]

for i in range(1,n):
  summary = summary + data[i]
  result.append(summary)

print(sum(result))


