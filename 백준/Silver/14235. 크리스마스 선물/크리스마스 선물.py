import sys
import heapq

input = sys.stdin.readline
n = int(input())
max_heap = []
answer = []

for _ in range(n):
    a_list = list(map(int, input().split()))
    a = a_list[0]

    if a == 0:
        if max_heap:
            gift = -heapq.heappop(max_heap)
            answer.append(gift)
        else:
            answer.append(-1)
    else:
        for value in a_list[1:]:
            heapq.heappush(max_heap, -value)
for i in answer:
  print(i)