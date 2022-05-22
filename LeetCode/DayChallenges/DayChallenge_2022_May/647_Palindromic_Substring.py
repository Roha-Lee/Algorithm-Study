class Solution:    
    def expandAndCountPallindromes(self, start, end, s):
        cnt=0
        while 0 <= start and end < len(s) and s[start] == s[end]:
            start-=1
            end+=1
            cnt+=1
        return cnt
        
    def countSubstrings(self, s: str) -> int:
        return sum(self.expandAndCountPallindromes(i,i,s) + self.expandAndCountPallindromes(i,i+1,s) for i in range(len(s)))