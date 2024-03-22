from collections import deque

def solution(n, wires):
    def bfs(s):
        count = 0
        
        queue = deque()
        visited = [0] * (n+1)
        
        queue.append(s)
        visited[s] = 1
        
        while queue:
            cur = queue.popleft()
            
            if arr[cur]:
                for nxt in arr[cur]:
                    if not visited[nxt]:
                        visited[nxt] = 1
                        queue.append(nxt)
                        count += 1
                        
        return count
        
    arr = [[] for _ in range(n+1)]
    for a, b in wires:
        arr[a].append(b)
        arr[b].append(a)
        
    answer = float('inf')  
    for a, b in wires:
        arr[a].remove(b)
        arr[b].remove(a)
        
        answer = min(answer, abs(bfs(a) - bfs(b)))
        
        arr[a].append(b)
        arr[b].append(a)
        
    return answer
