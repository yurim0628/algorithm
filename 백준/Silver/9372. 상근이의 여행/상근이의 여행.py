import sys
from collections import deque

def bfs(start, count):
  queue = deque()
  queue.append(start)
  visited[start] = True
  
  while queue:
    current = queue.popleft()
    for next in graph[current]:
      if not visited[next]:
        visited[next] = True
        queue.append(next)
        count += 1
        
  return count

T = int(input())
answer = []

for _ in range(T):
  N, M = map(int, input().split())
  visited = [False] * (N+1)
  graph = [[] for _ in range(N+1)]

  for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

  answer.append(bfs(1, 0))
print('\n'.join(map(str, answer)))