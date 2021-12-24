class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []
        for interval in sorted(intervals):
            if not results:
                results.append(interval)
                continue
                
            min_1, max_1 = results[-1]
            min_2, max_2 = interval
            
            if min_2 <= max_1:
                results.pop()
                results.append([min(min_1,min_2), max(max_1, max_2)])
            else:
                results.append(interval)
        return results