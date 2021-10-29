class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(31):
            ans = n & 1
            n >>= 1
            result |= ans
            result <<= 1
        result |= n
        return result
        
        