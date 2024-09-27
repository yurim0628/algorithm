N, M = map(int, input().split())
song_dict = {}

for _ in range(N):
    parts = input().split()
    title_length = int(parts[0])
    song_title = parts[1]
    first_three_notes = ''.join(parts[2:5])

    if first_three_notes in song_dict:
        song_dict[first_three_notes] = '?'
    else:
        song_dict[first_three_notes] = song_title

for _ in range(M):
    query_notes = ''.join(input().split())
    
    if query_notes in song_dict:
        print(song_dict[query_notes])
    else:
        print('!')