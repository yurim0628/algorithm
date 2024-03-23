def solution(word):
    char_list = ['A', 'E', 'I', 'O', 'U']
    count = 0
    
    def dfs(current_word):
        nonlocal count
        
        count += 1
        if current_word == word:
            return True 
        if len(current_word) == 5: 
            return False  
        for char in char_list:
            if dfs(current_word + char):
                return True  
        return False
    
    dfs("")
    return count - 1  
