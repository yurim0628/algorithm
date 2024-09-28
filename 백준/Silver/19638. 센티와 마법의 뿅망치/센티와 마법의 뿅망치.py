import sys
import heapq

input = sys.stdin.readline

n, h, t = map(int, input().split())
heights = []
count = 0

# 거인들의 키 입력받기
for _ in range(n):
    heapq.heappush(heights, -int(input()))  # 음수로 저장하여 최소 힙 사용

for j in range(t):
    max_height = -heapq.heappop(heights)  # 최대 키를 가져오기
    if max_height < h:
        print("YES")
        print(count)  # 사용한 횟수
        break
    elif max_height == 1:
        print("NO")
        print(1)  # 남은 횟수
        break
    else:
        heapq.heappush(heights, -(max_height // 2))  # 키를 절반으로 줄이기
        count += 1
else:
    max_height = -heapq.heappop(heights)  # 가장 큰 거인의 키 가져오기
    if max_height < h:
        print("YES")
        print(count)
    else:
        print("NO")
        print(max_height)  # 가장 큰 거인의 키 출력
