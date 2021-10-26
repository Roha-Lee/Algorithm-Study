class Solution:
    def _generate(self, curr, combinations, comb, n, k):
        if curr > n:
            return 
        if len(comb) == k:
            combinations.append(comb[:])
            return 
        
        for next in range(curr+1, n+1):
            comb.append(next)
            self._generate(next, combinations, comb, n, k)
            comb.pop()
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        self._generate(0, combinations, [], n, k)
        return combinations