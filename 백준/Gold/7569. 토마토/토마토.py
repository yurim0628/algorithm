from collections import deque
import sys

input = sys.stdin.read
data = input().splitlines()

M, N, H = map(int, data[0].split())

box = []
for h in range(H):
    layer = []
    for n in range(N):
        row = list(map(int, data[h * N + n + 1].split()))
        layer.append(row)
    box.append(layer)

queue = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                queue.append((h, n, m))

days = -1
while queue:
    length = len(queue)
    for _ in range(length):
        h, n, m = queue.popleft()
        for dh, dn, dm in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nh, nn, nm = h + dh, n + dn, m + dm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and box[nh][nn][nm] == 0:
                box[nh][nn][nm] = 1
                queue.append((nh, nn, nm))
    days += 1

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                print(-1)
                sys.exit()

print(days)
