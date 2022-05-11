class Solution:
    def countVowelStrings(self, n: int) -> int:
        DP = [1] * 5
        for _ in range(1, n):
            for i in range(1, 5):
                DP[i] = DP[i-1] + DP[i]
        return sum(DP)