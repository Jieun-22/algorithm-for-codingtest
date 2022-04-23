def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2 +1):
        string = ''
        prev = s[0:step]
        count = 1
        for i in range(step, len(s), step):
            if s[i:i+step] == prev:
                count += 1
            else:
                string += str(count) + prev if count >= 2 else prev
                prev = s[i:i+step]
                count = 1
        string += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(string))
    return answer
