from collections import deque 
class WordDictionary:
    def __init__(self):
        self.trie = dict()

    def addWord(self, word: str) -> None:
        curr = self.trie
        for letter in word:
            if letter in curr:
                curr = curr[letter]
            else:
                curr[letter] = dict()
                curr = curr[letter]
        curr['#'] = word

    def search(self, word: str) -> bool:
        next_q, q = deque([self.trie]), deque()
        for letter in word + '#':
            next_q, q = q, next_q
            while q:
                curr = q.popleft()
                if letter == '.':
                    for node in curr:
                        if not node == '#':
                            next_q.append(curr[node])
                else:
                    if letter in curr:
                        next_q.append(curr[letter])
            if not next_q:
                return False
            
        
        return True
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)