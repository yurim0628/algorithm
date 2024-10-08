import sys
from collections import deque

def bfs(start, end, mid_weight):
    visited = [False] * (N + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        if current == end:
            return True
        for next, weight in edges[current]:
            if not visited[next] and weight >= mid_weight:
                visited[next] = True
                queue.append(next)
    return False

def can_transport(mid_weight):
    return bfs(A, B, mid_weight)

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    edges[A].append((B, C))
    edges[B].append((A, C))

A, B = map(int, input().split())

low, high = 1, 1000000000
max_weight = 0

while low <= high:
    mid = (low + high) // 2
    if can_transport(mid):
        max_weight = mid
        low = mid + 1
    else:
        high = mid - 1

print(max_weight)
