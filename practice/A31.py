# 금광

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  
  array = []
  result = [[0]*(m+2) for _ in range(n+2)]
  data = list(map(int, input().split()))
  for i in range(n):
    array.append(data[i*m:i*m+m])

  for i in range(n):
    for j in range(m):
      result[i+1][j+1] = array[i][j]

  for j in range(1,m+1):
    for i in range(1, n+1):
      result[i][j] = result[i][j] +  max(result[i-1][j-1], result[i][j-1], result[i+1][j-1])


  max_value = 0

  for i in range(1,n+1):
    max_value = max(max_value, result[i][m])

  print(max_value)
    
