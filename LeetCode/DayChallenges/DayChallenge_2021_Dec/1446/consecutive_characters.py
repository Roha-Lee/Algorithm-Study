class Solution:
    def maxPower(self, s: str) -> int:
        max_val = 0
        val = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                val += 1
            else:
                max_val = max(max_val, val)
                val = 1
        return max(max_val, val)
            