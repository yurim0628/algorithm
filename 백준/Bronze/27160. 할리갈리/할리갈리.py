# 초기화
fruits = {'STRAWBERRY': 0, 'BANANA': 0, 'LIME': 0, 'PLUM': 0}

#  펼쳐진 카드의 개수 N을 입력받는다.
N = int(input())
for _ in range(N):
    # 과일의 종류를 나타내는 문자열 S와 과일의 개수를 나타내는 양의 정수 X를 입력받는다.
    S, X = input().split()
    # 입력받은 과일에 해당하는 과일의 개수를 추가한다.
    fruits[S] += int(X)

# 과일 개수 중 5인 것이 있는지 확인한다.
if any(value == 5 for value in fruits.values()):
    print('YES')
else:
    print('NO')