from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        arr = [(v, k) for k, v in counter.items()]
        arr = sorted(arr)
        result = []
        for _ in range(k):
            frq, val = arr.pop()
            result.append(val)
        return result
        