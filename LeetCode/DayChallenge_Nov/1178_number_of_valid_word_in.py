from itertools import combinations
from collections import Counter
class Solution:
    def generate_bitmask(self, word):
        mask = 0 
        for letter in word: 
            mask |= 1 << (ord(letter) - ord('a'))
        return mask 
  
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        words_masks = []
        
        for word in words:
            words_masks.append(self.generate_bitmask(word))
        counter = Counter(words_masks)
        answer = [0]  * len(puzzles)
        for i, puzzle in enumerate(puzzles):
            mask, first_letter = self.generate_bitmask(puzzle[1:]), self.generate_bitmask(puzzle[0])
            submask = mask 
            while submask: 
                answer[i] += counter[submask | first_letter]
                submask = (submask - 1) & mask
            answer[i] += counter[first_letter]
        return answer
                    
            