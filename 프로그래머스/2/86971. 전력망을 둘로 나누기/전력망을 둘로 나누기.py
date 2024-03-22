from collections import deque

def solution(n, wires):
    def bfs(s):
        count = 0
        
        queue = deque()
        visited = [False] * (n+1)
        
        queue.append(s)
        visited[s] = True
        
        while queue:
            cur = queue.popleft()
            for nxt in arr[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)
                    count += 1
        return count
        
    answer = float('inf')  
    for i, _ in enumerate(wires): 
        arr = [[] for _ in range(n+1)] 
        for j, wire in enumerate(wires): 
            if j != i: 
                arr[wire[0]].append(wire[1])
                arr[wire[1]].append(wire[0])
        min_diff = abs(bfs(wires[i][0]) - bfs(wires[i][1]))  
        answer = min(answer, min_diff)  
          
    return answer
