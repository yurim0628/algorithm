from collections import deque

def bfs(K, X, graph):
    answer = []
    visited = [0] * (N + 1)  # 방문 배열 초기화
    queue = deque([X])
    visited[X] = 1  # 시작 노드의 거리를 1로 설정

    while queue:
        C = queue.popleft()
        
        if visited[C] - 1 == K:  # K 거리 도달 확인
            answer.append(C)
        
        for neighbor in graph[C]:
            if visited[neighbor] == 0:  # 방문하지 않은 노드 확인
                visited[neighbor] = visited[C] + 1  # 거리 증가
                queue.append(neighbor)

    return answer

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

result = bfs(K, X, graph)  # BFS 호출로 result 정의

if result:
    result.sort()  # 결과를 오름차순으로 정렬
    print('\n'.join(map(str, result)))  # 각 도시 번호를 한 줄에 하나씩 출력
else:
    print(-1)
