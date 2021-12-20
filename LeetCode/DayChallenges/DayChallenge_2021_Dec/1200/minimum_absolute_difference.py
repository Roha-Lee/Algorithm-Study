class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        min_diff_list = []
        min_diff = 10000000
        
        for idx in range(1, len(arr)):
            curr_diff = arr[idx] - arr[idx-1]
            if min_diff > curr_diff:
                min_diff_list = []
                min_diff = curr_diff
                min_diff_list.append((arr[idx-1], arr[idx]))
            elif min_diff == curr_diff:
                min_diff_list.append((arr[idx-1], arr[idx]))
                
            
        return min_diff_list