# 숫자 카드 게임
  행에서 가장 작은 숫자를 뽑을 때 높은 수를 뽑는 프로그램

n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))

  min_value = min(data)
  result = max(result, min_value)

print(result)
