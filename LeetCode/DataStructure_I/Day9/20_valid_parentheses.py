class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_stack = []
        for letter in s:
            if letter in ['(','[','{']:
                parentheses_stack.append(letter)
            else:
                if not parentheses_stack:
                    return False
                current = parentheses_stack.pop()
                if letter == ']':
                    if not current == '[':
                        return False
                elif letter == ')':
                    if not current == '(':
                        return False
                elif letter == '}':
                    if not current == '{':
                        return False
        if parentheses_stack:
            return False
        return True