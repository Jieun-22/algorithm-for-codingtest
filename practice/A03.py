# 문자열 뒤집기

s = input()

result = 0

for i in range(len(s)-1):
  if s[i] != s[i+1]:
    result += 1

print(result-1)
