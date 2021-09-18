class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = dict()
        mag_dict = dict()

        for letter in ransomNote:
            ransom_dict.setdefault(letter, 0)
            ransom_dict[letter] += 1
        for letter in magazine:
            mag_dict.setdefault(letter, 0)
            mag_dict[letter] += 1

        for key in ransom_dict.keys():
            if not key in mag_dict:
                return False
            if ransom_dict[key] > mag_dict[key]:
                return False
        return True