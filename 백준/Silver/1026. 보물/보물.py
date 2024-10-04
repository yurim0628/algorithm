N = int(input())
A = sorted(map(int, input().split())) 
B = sorted(map(int, input().split()), reverse=True) 

print(sum(a * b for a, b in zip(A, B)))