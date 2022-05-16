/**
 * @param {number[][]} grid
 * @return {number}
 */
var shortestPathBinaryMatrix = function(grid) {
    let q = [];
    let nextQ = [];
    let pathLength = 1;
    const rows = grid.length;
    const cols = grid[0].length;
    const dR = [-1, 0, 1, -1, 1, -1, 0, 1];
    const dC = [-1, -1, -1, 0, 0, 1, 1, 1];
    
    if(grid[0][0] === 1 || grid[rows-1][cols-1] === 1) return -1;
    if(grid[0][0] === 0 && rows === 1 && cols === 1) return 1;
    if(grid[0][0] === 0) {
        q.push([0, 0]);
        grid[0][0] = 1;
    }
    
    while(q.length > 0) {
        for(const [r, c] of q) {
            for(let i = 0; i < 8; i += 1) {
                const nR = r + dR[i];
                const nC = c + dC[i];
                if(nR === rows - 1 && nC === cols - 1) {
                    return pathLength + 1;
                }
                if(0 <= nR && nR < rows && 0 <= nC && nC < cols && grid[nR][nC] === 0) {
                    grid[nR][nC] = 1;
                    nextQ.push([nR, nC]);
                }
            }
        }
        pathLength += 1;
        q = nextQ;
        nextQ = [];
    }
    return -1;
};