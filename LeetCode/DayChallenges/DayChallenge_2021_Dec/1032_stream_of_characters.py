from collections import deque

class StreamChecker:
    def __init__(self, words: List[str]):
        self.word_tree = dict()
        self.queue = deque()
        
        for word in words:
            curr = self.word_tree
            for letter in reversed(word):
                if letter not in curr:
                    curr[letter] = dict()
                curr = curr[letter]
            curr[0] = 0
            
    def query(self, letter: str) -> bool:
        self.queue.append(letter)
        curr = self.word_tree
        for letter in reversed(self.queue):
            if letter in curr:
                curr = curr[letter]
                if 0 in curr:
                    return True
            else:
                return False
        
        
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)