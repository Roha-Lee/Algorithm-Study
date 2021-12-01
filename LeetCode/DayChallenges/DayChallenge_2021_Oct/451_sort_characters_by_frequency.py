from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        q = [(-v, k) for k, v in cnt.items()]
        heapq.heapify(q)
        result = ''
        while q:
            v, k = heapq.heappop(q)
            result += k * -v
        return result
            