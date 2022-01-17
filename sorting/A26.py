n = int(input())

array = []

for i in range(n):
  array.append(int(input()))

array.sort()

result = [array[0] + array[1]]

if n >= 3:
  for i in range(2,n):
    result.append(result[i-2] + array[i])

print(sum(result))
  
  
