N = int(input()) * 4
working_hours = [4, 6, 4, 10]
workers = {}

for i in range(N):
    working_hour = working_hours[i % 4]  
    names = input().split() 
    for name in names:
        if name != "-":
            workers[name] = workers.get(name, 0) + working_hour

if workers:
    max_hours = max(workers.values())
    min_hours = min(workers.values())
    print("Yes" if max_hours - min_hours <= 12 else "No")
else:
    print("Yes")