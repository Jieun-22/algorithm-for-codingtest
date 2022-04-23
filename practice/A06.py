import heapq

def solution(food_times,k):
    answer = 0
    
    if sum(food_times) <= k:
        return -1
    
    q = []
    length = len(food_times)
    
    for i in range(length):
        heapq.heappush(q,(food_times[i],i+1))
        
    sum_value = 0 #현재까지 경과된 시간 
    previous = 0 # 직전에 다먹은 음식 시간
    
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0] 
        sum_value += (now-previous) * length
        length -= 1
        previous = now
        
    result = sorted(q, key = lambda x: x[1])
    return result[(k-sum_value) % length][1]

    
