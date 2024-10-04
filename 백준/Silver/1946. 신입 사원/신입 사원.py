import sys
input = sys.stdin.read
data = input().splitlines()

T = int(data[0])
index = 1
results = []

for _ in range(T):
    N = int(data[index])
    
    applicants = []
    for i in range(1, N + 1):
        doc, interview = map(int, data[index + i].split())
        applicants.append((doc, interview))
    
    applicants.sort()

    selected = 1
    min_interview_score = applicants[0][1]
    for i in range(1, N):
        if applicants[i][1] < min_interview_score:
            selected += 1
            min_interview_score = applicants[i][1]

    results.append(str(selected))
    index += N + 1

print("\n".join(results))
