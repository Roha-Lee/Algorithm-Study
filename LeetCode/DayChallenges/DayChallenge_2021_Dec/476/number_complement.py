class Solution:
    def findComplement(self, num: int) -> int:
        upper = 1
        while upper <= num:
            upper <<= 1
        return upper-1-num