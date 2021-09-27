class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = 0 if m == 0 else len(mat[0])
        if not r * c == m * n:
            return mat
        reshaped_mat = [[0] * c for _ in range(r)]
        for i in range(m):
            for j in range(n):
                one_dim_pos = i * n + j 
                re_i = int(one_dim_pos // c)
                re_j = one_dim_pos % c
                reshaped_mat[re_i][re_j] = mat[i][j] 
        return reshaped_mat