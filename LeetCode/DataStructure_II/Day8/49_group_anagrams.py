class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        type_dict = {}
        group_num = 0

        for word in strs:
            str_dict = dict()
            for letter in word:
                str_dict.setdefault(letter, 0)
                str_dict[letter] += 1
            str_key = str(sorted(str_dict.items()))
            type_dict.setdefault(str_key, -1)    
            if type_dict[str_key] == -1:
                results.append([word])
                type_dict[str_key] = group_num
                group_num += 1
            else:
                results[type_dict[str_key]].append(word)

        return results