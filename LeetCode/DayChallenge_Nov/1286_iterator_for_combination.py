class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combination_length = combinationLength
        self.combinations = []
        self.dfs(0)
        self.idx = 0
    def dfs(self, curr, result=[]):
        if len(result) == self.combination_length:
            self.combinations.append(result[:])
            return 
        for i in range(curr, len(self.characters)):
            result.append(self.characters[i]) 
            self.dfs(i + 1, result)
            result.pop()
        
    def next(self) -> str:        
        result = ''.join(self.combinations[self.idx])
        self.idx += 1
        return result
        

    def hasNext(self) -> bool:
        return self.idx < len(self.combinations)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()