def get_diff_count(word_a, word_b):
    return sum(1 for char_a, char_b in zip(word_a, word_b) if char_a != char_b)

def solution(begin, target, words):
    def dfs(begin, count):
        nonlocal min_count
        
        if begin == target:
            min_count = min(min_count, count)
            return
        
        for index, word in enumerate(words):
            if get_diff_count(begin, word) == 1 and not visited[index]:
                visited[index] = True
                dfs(word, count + 1)
                visited[index] = False

    min_count = float('inf')
    visited = [False] * len(words)            
    dfs(begin, 0)
    
    return min_count if min_count != float('inf') else 0
