class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.strip().split()
        if not len(pattern) == len(s):
            return False
        pattern_dict = dict()
        in_dict_words = []
        for pat, word in zip(pattern, s):
            if pat in pattern_dict:
                if not word == pattern_dict[pat]:
                    return False
            else:
                if word in in_dict_words:
                    return False
                pattern_dict[pat] = word
                in_dict_words.append(word)
        return True
        