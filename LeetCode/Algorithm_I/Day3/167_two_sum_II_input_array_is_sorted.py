class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        table = {number:idx for idx, number in enumerate(numbers)}
        for idx, num in enumerate(numbers):
            if target - num in table:
                first = min(idx+1, table[target-num]+1)
                second = max(idx+1, table[target-num]+1)
                return [first, second]

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, len(numbers)-1
        while s < e:
            val = numbers[s] + numbers[e]
            if target == val:
                return [s+1, e+1]
            elif target < val: 
                e -= 1
            else:
                s += 1
                
                