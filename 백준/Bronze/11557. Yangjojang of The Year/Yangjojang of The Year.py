T = int(input())
answers = []
university = []
for _ in range(T):
  N = int(input())
  for _ in range(N):
    university.append(list(input().split()))
  answers.append(sorted(university, key=lambda x:int(x[1]), reverse=True)[0])

for answer in answers:
  print(answer[0])
  