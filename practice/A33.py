# 퇴사

n = int(input())
data = []

for _ in range(n):
  data.append(list(map(int, input().split())))

dp = [0]*(n+1)
max_value = 0

for i in range(n-1,-1,-1):
  time = data[i][0] + i
  if time <= n :
    dp[i] = max(data[i][1] + dp[time], max_value)
    max_value = dp[i]
  else:
    dp[i] = max_value

print(max_value)
