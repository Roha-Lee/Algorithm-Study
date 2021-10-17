from collections import deque
class Solution:    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stack = []
        queue = deque()
        for num in nums:
            if num < 0:
                stack.append(num * num)
            else:
                queue.append(num * num)
        result = []
        qu = st = float("Inf")
        while stack or queue or st != float("Inf") or qu != float("Inf"):
            if stack and st == float("Inf"):
                st = stack.pop()
            if queue and qu == float("Inf"):
                qu = queue.popleft()
            
            if st < qu:
                result.append(st)
                if stack:
                    st = stack.pop()
                else:
                    st = float("Inf")
            else:
                result.append(qu)
                if queue:
                    qu = queue.popleft()
                else:
                    qu = float("Inf")
        return result
                
                