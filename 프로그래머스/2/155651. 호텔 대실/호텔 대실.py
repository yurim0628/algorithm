import heapq

def calculate_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes

def solution(book_time):
    room = [] 
    book_time.sort(key=lambda x: x[0])  

    for start_time, end_time in book_time:
        start_minutes = calculate_minutes(start_time)
        end_minutes = calculate_minutes(end_time)

        if room and room[0] <= start_minutes:
            heapq.heappop(room)

        heapq.heappush(room, end_minutes + 10)

    return len(room)
