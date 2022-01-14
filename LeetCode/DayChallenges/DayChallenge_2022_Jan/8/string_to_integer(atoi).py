class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        result = 0
        sign = 1
        idx = 0
        
        # remove white space
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        
        if idx >= len(s):
            return 0
        
        # check sign 
        if s[idx].isdigit(): 
            sign = 1
        elif s[idx] == '+':
            sign = 1
            idx += 1
        elif s[idx] == '-':
            sign = -1
            idx +=1 
        else:
            return 0
        
        if idx >= len(s):
            return 0
        
        # extract number 
        if not s[idx].isdigit():
            return 0
        min_num = -0x7fffffff - 1 
        max_num = 0x7fffffff
        
        while idx < len(s) and s[idx].isdigit():
            digit = ord(s[idx]) - 48
            if result <= (max_num - digit) / 10:
                result = result * 10 + digit
                idx += 1
            else:
                if sign > 0:
                    return max_num
                else:
                    return min_num
            
        
        return sign * result