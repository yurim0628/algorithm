def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 0: #삭제
            if a == 0: #기둥 삭제
                if [x, y+1, 0] in answer:
                    if not([x-1, y+1, 1] in answer or [x, y+1, 1] in answer): 
                        continue
                if [x-1, y+1, 1] in answer:
                    if not([x-1, y, 0] in answer or ([x-2, y+1, 1] in answer and [x, y+1, 1] in answer)):
                        continue
                if [x, y+1, 1] in answer:
                    if not([x+1, y, 0] in answer or ([x-1, y+1, 1] in answer and [x+1, y+1, 1] in answer)):
                        continue
                
                answer.remove([x, y, a])
                    
            if a == 1: #보 삭제   
                if [x, y, 0] in answer:
                    if not([x, y-1, 0] in answer or [x-1, y, 1] in answer): 
                        continue
                if [x+1, y, 0] in answer:
                    if not([x+1, y-1, 0] in answer or [x+1, y, 1] in answer):
                        continue
                if [x-1, y, 1] in answer:
                    if not([x, y-1, 0] in answer or [x-1, y-1, 0] in answer):
                        continue
                if [x+1, y, 1] in answer:
                    if not([x+1, y-1, 0] in answer or [x+2, y-1, 0] in answer):
                        continue
                answer.remove([x, y, a])
        if b == 1: #설치
            if a == 0: #기둥 설치
                if y == 0:
                    answer.append([x,y,a])
                else:
                    if [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                        answer.append([x,y,a])
            if a == 1: #보 설치
                if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                    answer.append([x, y, a])
                elif [x-1, y, 1] in answer and [x+1, y, 1] in answer:
                    answer.append([x, y, a])
                    
    answer.sort(key=lambda x: (x[0], x[1], x[2]))    
    return answer