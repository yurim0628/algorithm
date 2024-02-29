import math

def solution(fees, records):
    answer = []
    entry_dict = {}
    duration_dict = {}
    
    for item in records:
        record = item.split()
        time = record[0]
        number = record[1]
        check = record[2]
        
        if check == 'IN':
            entry_dict[number] = time
        if check == 'OUT':
            time2 = entry_dict[number]
            time2 = int(time2[:2]) * 60 + int(time2[3:])
            time = int(time[:2]) * 60 + int(time[3:])
            
            if number not in duration_dict:
                duration_dict[number] = time - time2
            else:
                duration_dict[number] += time - time2
            del entry_dict[number]
    
    for key, value in entry_dict.items():
        time = int(value[:2]) * 60 + int(value[3:])
        if key not in duration_dict:
            duration_dict[key] = 1439 - time
        else:
            duration_dict[key] += 1439 - time
    
    sorted_duration = sorted(duration_dict.items(), key=lambda x: x[0])
    
    for duration in sorted_duration:
        if duration[1] <= fees[0]:
            answer.append(fees[1])
        else:
            additional_duration = duration[1] - fees[0]
            additional_fee = math.ceil(additional_duration / fees[2]) * fees[3]
            answer.append(fees[1] + additional_fee)
    
    return answer
