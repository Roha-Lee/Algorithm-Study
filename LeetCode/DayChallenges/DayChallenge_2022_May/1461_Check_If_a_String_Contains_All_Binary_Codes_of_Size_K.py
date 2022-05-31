class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binary_code = set()
        for i in range(len(s) - k + 1):
            binary_code.add(int(s[i:i+k], 2))
        return len(binary_code) == 2 ** k
        