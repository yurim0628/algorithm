def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
     
    def dfs(k, count):
        nonlocal answer  
        answer = max(answer, count)
            
        for i, dungeon in enumerate(dungeons):
            if not visited[i] and k >= dungeon[0]:
                visited[i] = True
                dfs(k - dungeon[1], count + 1)
                visited[i] = False
    
    dfs(k, 0)
    return answer
