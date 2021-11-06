class Solution:
    def get_result(self, s):
        stack = []
        for letter in s: 
            if letter == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(letter)
        return ''.join(stack)
                
            
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.get_result(s) == self.get_result(t)
        