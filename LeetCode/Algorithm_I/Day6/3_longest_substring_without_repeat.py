class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        max_len = 0
        _len = len(s)
        for i in range(_len):
            contain = set()
            for j in range(i, _len):
                if s[j] in contain:
                    break
                contain.add(s[j])
                max_len = max(len(contain), max_len)
        return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        DP = [0] * (len(s) + 1)
        for i in range(len(s)):
            for j in range(i-DP[i-1], i):
                if s[i] == s[j]:
                    DP[i] = i - j
                    break
            if DP[i] == 0:
                DP[i] = DP[i-1] + 1 
        return max(DP)