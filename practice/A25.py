def solution(N, stages):
    
    answer = []
    
    data = [0]*(N+2)
    
    for x in stages:
        data[x] += 1
    
    length = len(stages)
    
    for i in range(1,N+1):
        if length != 0:
            answer.append((data[i]/length,i))
            length -= data[i]
        elif length == 0:
            answer.append((0,i))
      
    answer.sort(key = lambda x: (-x[0], x[1]))
    for i in range(len(answer)):
        answer[i] = answer[i][1]
        
        
    return answer


