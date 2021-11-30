class Solution:
    def get_maximum_rectangle(self, heights):
        stack = [-1]
        max_area = 0
        for idx in range(len(heights)):
            while len(stack) > 1 and heights[stack[-1]] >= heights[idx]:
                loc = stack.pop()
                max_area = max((idx - 1 - stack[-1]) * heights[loc], max_area)
            stack.append(idx)
            
        while len(stack) > 1: 
            loc = stack.pop()
            max_area = max(max_area, (len(heights) - 1 - stack[-1]) * heights[loc])
        return max_area
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        if not rows: return 0
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0
            max_area = max(max_area, self.get_maximum_rectangle(heights)) 
        return max_area