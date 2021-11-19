class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_val = x^y
        bit_count = 0
        while xor_val > 0:
            bit_count += xor_val & 1
            xor_val >>= 1
        return bit_count