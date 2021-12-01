from collections import Counter
class DisjointSet:
    def __init__(self, nums):
        self.parents = {num:num for num in nums}
        self.ranks = {num:0 for num in nums}
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.ranks[x] < self.ranks[y]:
                self.parents[x] = self.parents[y]
                self.ranks[x] = self.ranks[y]
            elif self.ranks[x] == self.ranks[y]:
                self.parents[x] = self.parents[y]
                self.ranks[x] += 1
            else:
                self.parents[y] = self.parents[x]
                self.ranks[y] = self.ranks[x]
                            
        
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ds = DisjointSet(nums)
        max_num = max(nums)
        sieve = [1] * (max_num + 1)
        for i in range(2, max_num // 2 + 1):
            if sieve[i]:
                left = None
                if i in nums_set:
                    left = i
                    
                for j in range(2, max_num // i + 1):
                    val = i*j
                    sieve[val] = 0
                    if not left and val in nums_set:
                        left = val 
                    elif left and val in nums_set:
                        ds.union(left, val)
        
        for num in nums:
            ds.find(num)
            
        return Counter(ds.parents.values()).most_common()[0][1]
                
                