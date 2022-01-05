class Solution:
    def is_palindrome(self, s):
        for i in range(len(s)//2):
            if not s[i] == s[-i-1]:
                return False
        return True
    
    def gen_result(self, palin_info, s, curr, result, results):
        if curr >= len(s):
            results.append(result[:])
            return 
        
        for palin in palin_info[curr]:    
            result.append(palin)
            self.gen_result(palin_info, s, curr + len(palin), result, results)
            result.pop()
        
    def partition(self, s: str) -> List[List[str]]:
        palin_info = [[] for _ in range(len(s))]
        for start in range(len(s)):
            for end in range(start+1, len(s)+1):
                sliced = s[start:end]
                if self.is_palindrome(sliced):
                    palin_info[start].append(sliced)
        results = []
        self.gen_result(palin_info, s, 0, [], results)
        return results
            
        