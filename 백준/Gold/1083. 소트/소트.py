n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n):
    number = max(arr[i : min(n, i + s + 1)])
    index = arr.index(number)

    if index == i:
        continue
    
    arr.pop(index)
    arr.insert(i, number)
    
    s -= (index - i)
    if s == 0:
        break

print(*arr)
