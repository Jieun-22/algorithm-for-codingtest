# 고정점 찾기

n = int(input())
data = list(map(int, input().split()))

def binary_search(array, start, end):

  while start <= end:
    mid = (start+end)//2

    if array[mid] == mid:
      return mid
    elif array[mid] < mid:
      start = mid +1
    else:
      end = mid -1
  
  return -1

result = binary_search(data, 0, n)

print(result)

