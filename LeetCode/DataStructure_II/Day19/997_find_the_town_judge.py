class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        
        pmap = {p:set() for p in range(1, n+1)}
        for left, right in trust:
            pmap[left].add(right)
        
        judge = None
        for k in pmap.keys():
            if not pmap[k]:
                for p in pmap.keys():
                    if p == k:
                        continue
                    if not k in pmap[p]:
                        judge = None
                        break
                    else:
                        judge = k
        if judge:
            return judge
        return -1
        