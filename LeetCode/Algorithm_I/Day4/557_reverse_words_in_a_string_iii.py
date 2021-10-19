class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        results = []
        for word in words:
            list_word = list(word)
            list_word.reverse()
            results.append(''.join(list_word))
        return ' '.join(results)
            
        