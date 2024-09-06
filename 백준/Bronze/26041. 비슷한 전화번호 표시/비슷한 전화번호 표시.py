# 첫 번째 줄에 문자열 A가 주어진다.
# 두 번째 줄에 전화번호 B가 주어진다.
A = input().split()
B = input()

# count는 결과를 저장시킬 변수이다.
count = 0

# 1. 문자열 A에 포함된 전화번호 중에서 
# 2. 전화번호 B와 다르면서 B를 접두사로 갖는 전화번호가 있다면 
# 3. 카운트를 증가시킨다.
for phone_number in A:
    if phone_number != B and phone_number.startswith(B):
        count += 1

# 결과를 출력한다.
print(count)