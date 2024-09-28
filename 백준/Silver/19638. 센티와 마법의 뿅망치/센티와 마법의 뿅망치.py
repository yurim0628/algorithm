import sys
import heapq

input = sys.stdin.readline

n, h, t = map(int, input().split())

heights = []
count = 0

for _ in range(n):
    heapq.heappush(heights, -int(input())) 

for _ in range(t):
    max_height = -heapq.heappop(heights) 
    if max_height < h:
        print("YES")
        print(count)  
        break
    if max_height > 1:
        heapq.heappush(heights, -(max_height // 2))  
        count += 1
    else:
        print("NO")
        print(1)
        break
     
else:
    max_height = -heapq.heappop(heights) 
    if max_height < h:
        print("YES")
        print(count)
    else:
        print("NO")
        print(max_height) 
