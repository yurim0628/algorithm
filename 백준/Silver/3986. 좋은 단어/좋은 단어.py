n = int(input())
good_word_count = 0

for _ in range(n):
    stack = []
    word = list(input())
    
    for char in word:
        if not len(stack):
            stack.append(char)
        elif stack[-1] == char:
            stack.pop(-1)
        else:
            stack.append(char)

    if not len(stack):
        good_word_count += 1 

print(good_word_count)