class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()

        for letter in s:
            s_dict.setdefault(letter, 0)
            s_dict[letter] += 1
        for letter in t:
            t_dict.setdefault(letter, 0)
            t_dict[letter] += 1
        if not s_dict.keys() == t_dict.keys():    
            return False
        for s_key in s_dict.keys():
            if not s_dict[s_key] == t_dict[s_key]:
                return False
        return True