class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ''
        a, b = a[::-1], b[::-1]
        rev_a = max(a, b, key=lambda x:len(x))
        rev_b = b if rev_a == a else a
        carry, add = 0, 0
        for idx in range(len(rev_b)):
            add = int(rev_a[idx]) + int(rev_b[idx]) + carry
            carry, add = add // 2, add % 2
            result += str(add)
            
        for idx in range(len(rev_b), len(rev_a)):
            add = int(rev_a[idx]) + carry    
            carry, add = add // 2, add % 2
            result += str(add)
        
        if carry:
            result += str(carry)
            
        return result[::-1]