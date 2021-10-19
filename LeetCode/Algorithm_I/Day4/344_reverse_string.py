class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        mid = n // 2
        
        for i in range(mid):
            s[i], s[n-i-1] = s[n-i-1], s[i]
        