class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        remains = [0] * len(gas)
        for i in range(1, len(gas)):
            remains[i] = remains[i-1] + gas[i-1] - cost[i-1]
        
        return remains.index(min(remains))