class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0: return 1
        mask = 1
        copy_n = n
        while copy_n:
            copy_n >>= 1
            mask <<= 1
        return ~n & (mask - 1)