class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_dict = dict()
        words = s.split()
        used_words = set()
        if len(pattern) != len(words):
            return False
        
        for idx, letter in enumerate(pattern):
            if letter in word_dict:
                if word_dict[letter] != words[idx]:
                    return False
            elif letter not in word_dict:
                if words[idx] in used_words:
                    return False
                word_dict[letter] = words[idx]
                used_words.add(words[idx])
            
        return True