n, k = map(int, input().split())
experiences = list(map(int, input().split()))
experiences.sort()

answer = 0
for i in range(k):
    answer += experiences[i] * i
for j in range(k, n):
    answer += experiences[j] * k

print(answer)