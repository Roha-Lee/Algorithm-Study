from collections import Counter 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_s, cnt_p = Counter(s[:len(p)]), Counter(p)
        result = []
        for i in range(len(s) - len(p)):
            if cnt_s == cnt_p:
                result.append(i)
            cnt_s[s[i]] -= 1
            cnt_s[s[i+len(p)]] += 1
        if cnt_s == cnt_p:
            result.append(len(s) - len(p))
        return result