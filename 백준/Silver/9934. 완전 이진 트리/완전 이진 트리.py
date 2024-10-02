k = int(input())
nodes = list(map(int, input().split()))
levels = [[] for _ in range(k)]

def tree(nodes, level):
    if not nodes: 
        return
    middle = len(nodes) // 2
    levels[level].append(nodes[middle])  
    tree(nodes[:middle], level + 1)  
    tree(nodes[middle + 1:], level + 1) 

tree(nodes, 0)

for level in levels:
    print(" ".join(map(str, level)))  
