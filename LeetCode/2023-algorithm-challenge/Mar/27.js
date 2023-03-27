/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    const m = grid.length;
    const n = grid[0].length;
    let r, s, c;
    for (s = 0; s < m + n; s += 1) {
        for (c = 0; c <= s; c += 1) {
            r = s - c;
            if (r < 0 || r >= m || c < 0 || c >= n) continue;
            if (r === 0 && c === 0) continue;
            if (r === 0) {
                grid[r][c] += grid[r][c-1];
                continue;
            } 
            if (c === 0) {
                grid[r][c] += grid[r-1][c];
                continue;
            }
            grid[r][c] += Math.min(grid[r][c-1], grid[r-1][c]);
        }
    }
    return grid[m-1][n-1];
    
};
