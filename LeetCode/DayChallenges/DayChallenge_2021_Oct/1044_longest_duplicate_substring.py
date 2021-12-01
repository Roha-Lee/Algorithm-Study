from collections import defaultdict
class Solution:
    def RabinKarp(self, s, length):
        hash_table = defaultdict(list)
        hs = 26
        multiplicant = 1
        q = (1 << 31) - 1
        val = 0
        for i in range(length):
            multiplicant = (multiplicant * hs) % q
            val = ((val * hs) % q + ord(s[i]) - ord('a')) % q
        hash_table[val].append(0)
        for i in range(1, len(s) - length + 1):
            val = (val * hs) % q 
            val = (val - ((ord(s[i-1]) - ord('a')) * multiplicant)) % q
            val = (val + (ord(s[i+length-1]) - ord('a'))) % q
            rclip = s[i:i+length]
            
            for idx in hash_table[val]:
                lclip = s[idx:idx+length]
                if lclip == rclip:
                    return rclip
            hash_table[val].append(i)
        
    def longestDupSubstring(self, s: str) -> str:
        start = 1
        end = len(s)-1
        result = ""
        while start <= end: 
            mid = (start + end) // 2
            
            temp_result = self.RabinKarp(s, mid)
            if temp_result:
                result = temp_result
                start = mid + 1
            else:
                end = mid - 1
        return result
        