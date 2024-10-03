from collections import deque

T = int(input())
answer = []

for i in range(T):
    if i != T: 
        input()

    N, M = map(int, input().split())
    sejun = deque(sorted(map(int, input().split())))
    sebi = deque(sorted(map(int, input().split())))

    while sejun and sebi:
        sejun.popleft() if sejun[0] < sebi[0] else sebi.popleft()

    result = 'S' if sejun else 'B' if sebi else 'C'
    answer.append(result)

print('\n'.join(answer))