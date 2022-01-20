# 고정점 찾기

n = int(input())
data = list(map(int, input().split()))

def binary_search(array, start, end):

  while start <= end:
    mid = (start+end)//2
    target = mid

    if array[mid] == target:
      return mid
    elif array[mid] < target:
      start = mid +1
    else:
      end = mid -1
  
  return -1

result = binary_search(data, 0, n)

print(result)

