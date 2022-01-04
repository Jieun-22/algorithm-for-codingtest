def dfs(graph, v, visited):
  #현재노드 방문처리
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      #방문하지 않은 경우 재귀적으로 방문
      dfs(graph, i, visited)

graph = [
         [],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]
]

visited = [False] * 9

dfs(graph,1,visited)
