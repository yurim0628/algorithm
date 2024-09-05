n = int(input())
prev = ['*']
count_star = 1

for _ in range(1, n):
    current = []
    count_star += 4  
    current.append('*' * count_star) 
    current.append('*' + ' ' * (count_star - 2) + '*') 

   
    for i in range(len(prev)):
        current.append('* ' + prev[i] + ' *')

    current.append('*' + ' ' * (count_star - 2) + '*') 
    current.append('*' * count_star)  

    prev = current  

for line in prev:
    print(line)