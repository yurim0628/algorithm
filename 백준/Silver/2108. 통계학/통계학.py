from collections import Counter

N = int(input())
integers = [int(input()) for _ in range(N)]

avg = round(sum(integers) / N)
integers.sort()
mid = integers[N // 2]

count = Counter(integers)
most_common = count.most_common()

if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    mode = most_common[1][0]
else:
    mode = most_common[0][0]

range_value = integers[-1] - integers[0]

answer = [avg, mid, mode, range_value]
print('\n'.join(map(str, answer)))
