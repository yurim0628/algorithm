T = int(input()) # 테스트 케이스의 개수 T를 입력받는다.
for _ in range(T):
    R, S = input().split()  # 각 줄에서 반복 횟수 R과 문자열 S를 입력받는다.
    print(''.join([C * int(R) for C in S]))  # 각 문자 C를 R만큼 반복하여 출력한다.