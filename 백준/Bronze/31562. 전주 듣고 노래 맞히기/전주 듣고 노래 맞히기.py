N, M = map(int, input().split())
dic = {}

for _ in range(N):
    parts = input().split()
    title = parts[1]
    notes = ''.join(parts[2:5])
    dic[notes] = '?' if notes in dic else title

for _ in range(M):
    input_notes = ''.join(input().split())
    print(dic.get(input_notes, '!'))