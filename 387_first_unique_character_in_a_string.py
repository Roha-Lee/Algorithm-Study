class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_dict = dict()

        for index, letter in enumerate(s):
            letter_dict.setdefault(letter, [index, 0])
            letter_dict[letter][1] += 1 

        min_index = len(s)
        for key, value in letter_dict.items():
            if letter_dict[key][1] == 1 and letter_dict[key][0] < min_index:
                min_index = letter_dict[key][0]
        min_index = -1 if len(s) == min_index else min_index
        return min_index
        