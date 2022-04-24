#26 카드 정렬하기

n = int(input())

data = []
for _ in range(n):
  data.append(int(input()))

data.sort()

sum = data[0]
answer = 0

for i in range(1, len(data)):
  sum += data[i]
  answer += sum

print(answer)
