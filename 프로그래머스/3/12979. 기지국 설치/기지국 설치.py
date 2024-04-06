def solution(n, stations, w):
    answer = 0

    current_position = stations[0]
    while current_position > w + 1:
        answer += 1
        current_position -= 2 * w + 1
    
    current_position = stations[0]
    for station in stations[1:]:
        while current_position + w + 1 < station - w:
            answer += 1
            current_position += 2 * w + 1
        current_position = station
        
    while current_position < n - w:
        answer += 1
        current_position += 2 * w + 1

    return answer