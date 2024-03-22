from collections import deque

def solution(n, computers):
    count = 0
    arr = [[] for _ in range(n)]
    visited = [False] * n
    
    def bfs(i):
        queue = deque()
        queue.append(i)
        visited[i] = True
        
        while queue:
            cur = queue.popleft()
            
            if arr[cur]:
                for nxt in arr[cur]:
                    if not visited[nxt]:
                        queue.append(nxt)
                        visited[nxt] = True
                        
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                arr[i].append(j)
            
    for i in range(n):
        if not visited[i]:
            bfs(i)
            count += 1
        
    return count
