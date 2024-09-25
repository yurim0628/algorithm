from collections import deque
import sys

input = sys.stdin.read
data = input().splitlines()

answer = deque()  # 덱 초기화
result = []  # 결과 저장 리스트

for command in data[1:]:
    if "push_front" in command:
        answer.appendleft(command.split()[1])
    elif "push_back" in command:
        answer.append(command.split()[1])
    elif command == "pop_front":
        result.append(answer.popleft() if answer else -1)
    elif command == "pop_back":
        result.append(answer.pop() if answer else -1)
    elif command == "size":
        result.append(len(answer))
    elif command == "empty":
        result.append(0 if answer else 1)
    elif command == "front":
        result.append(answer[0] if answer else -1)
    elif command == "back":
        result.append(answer[-1] if answer else -1)

sys.stdout.write("\n".join(map(str, result)) + "\n")