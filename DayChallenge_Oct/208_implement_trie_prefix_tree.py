class Trie:
  
    def __init__(self):
        self.root = dict()
        
    def insert(self, word: str) -> None:
        curr = self.root
        word += '0'
        for letter in word:
            curr.setdefault(letter, dict())
            curr = curr[letter]
        
    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter in curr:
                curr = curr[letter]
            else:
                return False
        return '0' in curr
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix: 
            if letter in curr:
                curr = curr[letter]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)