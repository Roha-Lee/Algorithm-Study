class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]*(i+1) for i in range(numRows)]
        for rows in range(2, numRows):
            for i in range(1, rows):
                result[rows][i] = result[rows-1][i-1] + result[rows-1][i]  

        return result