def solution(tickets):
    def dfs(current, path):
        nonlocal answer
        
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return
        
        if current in dict:
            for i, dest in enumerate(dict[current]):
                if not visited[current][i]:
                    visited[current][i] = True
                    dfs(dest, path + [dest])
                    visited[current][i] = False

    answer = []
    dict = {}
    visited = {}

    for start, end in tickets:
        if start not in dict:
            dict[start] = []
            visited[start] = []
        dict[start].append(end)
        visited[start].append(False)
        
    for key in dict:
        dict[key].sort()

    dfs("ICN", ["ICN"])
    
    return answer[0]
