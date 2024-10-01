n, act = map(int, input().split())  

k = list(map(int, input().split()))  
k.sort()  

cnt, exp = 0, 0  

for i in range(n):
    if cnt < act:
        cnt += 1  
        exp -= k[i] 
    exp += k[i] * cnt  
print(exp)  