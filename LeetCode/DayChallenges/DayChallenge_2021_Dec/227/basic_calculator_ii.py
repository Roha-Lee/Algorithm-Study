from operator import add, sub, mul, floordiv

class Solution:
    def calculate(self, s: str) -> int:
        op_dict = {'+':add, '-':sub, '*':mul, '/':floordiv}
        num_stack = []
        op_stack = []
        num = ""
        doit_now = None
        s+='.'
        s = s.replace(' ', '')
        for letter in s:
            if letter.isdigit():
                num += letter
                continue    
            num_stack.append(int(num))
            num = ""
            if doit_now:
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                num_stack.append(doit_now(num2, num1))
                doit_now = None

            if letter == '*' or letter == '/':
                doit_now = op_dict[letter]
            else:
                if letter == '.':
                    break
                op_stack.append(op_dict[letter])
        
        op_stack.reverse()
        num_stack.reverse()
        while op_stack:
            num1 = num_stack.pop()
            num2 = num_stack.pop()
            num_stack.append(op_stack.pop()(num1, num2))
        return num_stack[0]
