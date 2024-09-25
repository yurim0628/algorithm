from collections import deque
import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
dq = deque()

result = []
for i in range(1, n + 1):
    command = data[i].split()
    
    if command[0] == "push_front":
        dq.appendleft(int(command[1]))
    elif command[0] == "push_back":
        dq.append(int(command[1]))
    elif command[0] == "pop_front":
        if dq:
            result.append(dq.popleft())
        else:
            result.append(-1)
    elif command[0] == "pop_back":
        if dq:
            result.append(dq.pop())
        else:
            result.append(-1)
    elif command[0] == "size":
        result.append(len(dq))
    elif command[0] == "empty":
        result.append(1 if not dq else 0)
    elif command[0] == "front":
        if dq:
            result.append(dq[0])
        else:
            result.append(-1)
    elif command[0] == "back":
        if dq:
            result.append(dq[-1])
        else:
            result.append(-1)

sys.stdout.write("\n".join(map(str, result)) + "\n")
