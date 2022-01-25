class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: 
            return False
        diff_arr = [arr[i] - arr[i+1] for i in range(len(arr) - 1)]
        idx = 0
        while idx < len(diff_arr) and diff_arr[idx] < 0:
            idx += 1
        
        if idx == len(diff_arr) or idx == 0:
            return False
        
        while idx < len(diff_arr) and diff_arr[idx] > 0:
            idx += 1
            
        return idx == len(diff_arr)