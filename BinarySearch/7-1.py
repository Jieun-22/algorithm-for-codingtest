# 순차 탐색 소스 코드 구현

def sequential_search(n, target, array):
  for i in range(n):
    if array[i] == target :
      return i+1
