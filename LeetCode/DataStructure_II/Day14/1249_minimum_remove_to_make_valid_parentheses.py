class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        letter_list = list(s)
        
        score = 0
        stack = []
        removed = []
        for i in range(len(letter_list)-1, -1, -1):
            letter = letter_list[i]
            if letter == ')':
                score += 1
                stack.append(i)
            elif letter == '(':
                score -= 1
                if score < 0:
                    removed.append(i)
                    score += 1
                if stack:
                    stack.pop()
                    
        remove_index = set(stack + removed)
        letter_list = [letter for idx, letter in enumerate(letter_list) if idx not in remove_index]
        return ''.join(letter_list)
                    