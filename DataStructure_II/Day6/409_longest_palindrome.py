class Solution:
    def longestPalindrome(self, s: str) -> int:
        alpha_dict = dict()
        for letter in s:
            alpha_dict.setdefault(letter, 0)
            alpha_dict[letter] += 1
        
        result = 0
        odd_exist = 0
        for k, v in alpha_dict.items():
            if v % 2 == 0:
                result += v
            else:
                odd_exist = 1
                result += v-1
        
        return result + odd_exist
            
        