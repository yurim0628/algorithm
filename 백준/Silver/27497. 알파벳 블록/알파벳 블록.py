import sys
from collections import deque

input = sys.stdin.readline

answer = deque()
direction = []

N = int(input())

for _ in range(N):
    line = input().split()

    if line[0] == '3':
        if direction:
            if direction.pop() == 'back':
                answer.pop()  # 맨 뒤의 블록 제거
            else:
                answer.popleft()  # 맨 앞의 블록 제거
    elif line[0] == '1':
        answer.append(line[1])  # 문자열 맨 뒤에 추가
        direction.append('back')
    elif line[0] == '2':
        answer.appendleft(line[1])  # 문자열 맨 앞에 추가
        direction.append('front')

# 결과 출력
print(''.join(answer) if answer else '0')
