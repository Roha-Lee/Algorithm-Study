class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_info = [(set(word), len(word)) for word in words]
        words_info = sorted(words_info, key=lambda x: x[1], reverse = True)
        max_value = 0
        for i in range(len(words_info)):
            for j in range(i+1, len(words_info)):
                if not len(words_info[i][0].intersection(words_info[j][0])):
                    max_value = max(max_value, words_info[i][1] * words_info[j][1])
        return max_value
        
        