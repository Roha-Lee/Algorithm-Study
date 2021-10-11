class Solution:
    def DFS(self, results, candidates, n):
        if n == len(candidates):
            results.append(candidates[:])
            return 
        for new_col in range(n):
            if self.is_available(new_col, candidates):
                candidates.append(new_col)
                self.DFS(results, candidates, n)
                candidates.pop()

    def is_available(self, col, candidates):
        if col in candidates:
            return False
        row = len(candidates)
        for qrow, qcol in enumerate(candidates):
            if abs(qcol - col) == row - qrow:
                return False
        return True
    
    def decorate_result(self, results, n):
        decorated_results = []
        
        for result in results:
            decorated = []
            for elem in result:
                template = ['.']*(n-1)
                template.insert(elem, 'Q')
                decorated.append(''.join(template))
            decorated_results.append(decorated)
        return decorated_results
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        self.DFS(results, [], n)
        return self.decorate_result(results, n)