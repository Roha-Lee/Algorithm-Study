class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_row = len(matrix)
        target_i = -1
        for i in range(num_row):
            if target >= matrix[i][0]:
                target_i = i
        if target_i == -1:
            return False

        # binary search 
        def search(arr, target):
            if len(arr) == 0:
                return False
            if len(arr) == 1:
                if arr[0] == target:
                    return True
                return False
            else:
                right_start = int(len(arr) // 2)
                if arr[right_start] <= target:
                    right_half = arr[right_start:]
                    return search(right_half, target)
                else:
                    left_half = arr[:right_start] 
                    return search(left_half, target)

        return search(matrix[target_i], target)
