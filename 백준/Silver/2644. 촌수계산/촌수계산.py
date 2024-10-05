from collections import deque

n = int(input())
start, end = map(int, input().split())
m = int(input())

visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = 1
  while queue:
    current = queue.popleft()
    if current == end:
      return visited[current] - 1
    for next in graph[current]:
      if not visited[next]:
        queue.append(next)
        visited[next] = visited[current] + 1
  return -1

print(bfs(graph, start, visited))