class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x:x[1])
        removed = 0
        end = sorted_intervals[0][1]
        for interval in sorted_intervals[1:]:
            if end <= interval[0]:
                end = interval[1]
            else:
                removed+=1
        return removed