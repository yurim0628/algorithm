def solution(genres, plays):
    answer = []
    
    genre_songs = {} 
    genre_plays = {}  
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_songs:
            genre_songs[genre] = [[i, play]]
            genre_plays[genre] = play
        else:
            genre_songs[genre].append([i, play])
            genre_plays[genre] += play
    
    sorted_genres = sorted(genre_plays.keys(), key=lambda x: -genre_plays[x])
    
    for genre in sorted_genres: 
        sorted_songs = sorted(genre_songs[genre], key=lambda x: -x[1])[:2]
        for song in sorted_songs:
            answer.append(song[0])
    
    return answer
