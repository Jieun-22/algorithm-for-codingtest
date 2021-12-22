# 문자열 압축

s = input()

answer = len(s)

for step in range(1, len(s)//2 + 1):
  compressed = ''
  prev = s[0:step]
  count = 1

  for j in range(step, len(s), step):
    if prev == s[j: j+step]:
      count += 1
    else:
      compressed += str(count) + prev if count >= 2 else prev
      prev = s[j:j+step]
      count = 1
  # 남아있는 문자열에 대해서 처리
  compressed += str(count) + prev if count >= 2 else prev
  answer = min(answer, len(compressed))

print(answer) 
