class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for letter in s: 
            if letter == ']':
                result = ''
                while not stack[-1] == '[':
                    result = stack.pop() + result
                stack.pop()
                
                mult = ''
                while stack and stack[-1].isdigit():
                    mult = stack.pop() + mult
                result *= int(mult)
                stack.append(result)
            else:
                stack.append(letter)
        return ''.join(stack)