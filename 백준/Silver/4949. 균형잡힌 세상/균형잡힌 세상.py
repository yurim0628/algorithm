import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break

    stack = []
    is_balanced = True
    
    for letter in sentence:
        if letter in "([":  # 왼쪽 괄호
            stack.append(letter)
        elif letter == ")":  # 오른쪽 소괄호
            if not stack or stack[-1] != "(":
                is_balanced = False
                break
            stack.pop()
        elif letter == "]":  # 오른쪽 대괄호
            if not stack or stack[-1] != "[":
                is_balanced = False
                break
            stack.pop()

    if is_balanced and not stack:
        print('yes')
    else:
        print('no')