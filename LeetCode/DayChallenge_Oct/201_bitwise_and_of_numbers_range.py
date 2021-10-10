class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        mult = 1
        while left != right:
            left //= 2
            right //= 2
            mult *= 2
        return left * mult
                