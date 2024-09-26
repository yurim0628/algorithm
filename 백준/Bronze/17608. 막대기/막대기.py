import sys

input = sys.stdin.readline
N = int(input())
stack = [int(input()) for _ in range(N)] 
max_num = 0
answer = 0

for i in range(N - 1, -1, -1):
    if stack[i] > max_num:
        max_num = stack[i]
        answer += 1

print(answer)

