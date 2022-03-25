#  곱하기 혹은 더하기

s = input()

result = int(s[0])

for i in range(1, len(s)):
  num = int(s[i])
  if result == 0 or result == 1 :
    result += num
  else:
    if num == 0 and num == 1:
      result += num
    else:
      result *= num

print(result)

