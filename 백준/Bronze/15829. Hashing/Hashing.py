L = int(input()) 
string = input() 

r = 31
M = 1234567891

sum = 0
cnt = 0
for s in string:
    i = ord(s)-96
    sum += (i * r**cnt) % M 
    cnt += 1

sum %= M
print(sum)