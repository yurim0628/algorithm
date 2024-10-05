import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 1

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N + 1):
    graph[i].sort()

def dfs(graph, visited, current):
    global count
    visited[current] = count
    count += 1
    for next in graph[current]:
        if not visited[next]:
            dfs(graph, visited, next)

dfs(graph, visited, R)
print('\n'.join(map(str, visited[1:])))