class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_dict = dict()
        for idx, letter in enumerate(s):
            letter_dict.setdefault(letter, [])
            letter_dict[letter].append(idx)
        intervals = [value for _, value in letter_dict.items()]
        intervals = self.merge_interval(sorted(intervals))
        return self.get_length(intervals)
    
    def merge_interval(self, intervals: List[List[int]]) -> List[int]:
        int_max = intervals[0][-1]
        int_min = intervals[0][0]
        new_intervals = []
        
        for interval in intervals[1:]:
            new_max, new_min = interval[-1], interval[0]
            if new_min <= int_max:
                int_max = max(int_max, new_max)
            else:
                new_intervals.append([int_min, int_max])
                int_min, int_max = interval[0], interval[-1]
                
        new_intervals.append([int_min, int_max])
        return new_intervals
    
    def get_length(self, intervals: List[List[int]]) -> List[int]:
        return [intv[-1] - intv[0] + 1 for intv in intervals]
            
        