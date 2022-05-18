/**
 * @param {number[][]} grid
 * @param {number} tR
 * @param {number} tC
 * @return {number}
 */
 const getAreaOfIsland = function(grid, r, c, area = 0) {
    if(grid[r][c] === 0) return area;
    const numRow = grid.length;
    const numCol = grid[0].length;
    const dR = [0, 1, 0, -1];
    const dC = [1, 0, -1, 0];
    let nR;
    let nC;
    grid[r][c] = 0;
    area += 1;
    for(let i = 0; i < 4; i += 1) {
        nR = r + dR[i];
        nC = c + dC[i];
        if(nR < 0 || nR >= numRow || nC < 0 || nC >= numCol) continue;
        area = getAreaOfIsland(grid, nR, nC, area);
    }
    return area;
}
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
    const numRow = grid.length;
    const numCol = grid[0].length;
    let maxArea = 0;
    for(let r = 0; r < numRow; r += 1) {
        for(let c = 0; c < numCol; c += 1) {
            if(grid[r][c] === 1) {
                maxArea = Math.max(maxArea, getAreaOfIsland(grid, r, c));
            }
        }
    }
    return maxArea;
};

