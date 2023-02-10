/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxDistance = function(grid) {
    let queue = [];
    const maxR = grid.length;
    const maxC = grid[0].length;
    for (let r = 0; r < maxR; r += 1) {
        for (let c = 0; c < maxC; c += 1) {
            if (grid[r][c]) {
                queue.push([r, c]);
            } 
        }
    }
    let nextQueue = [];
    const directionR = [0, 1, 0, -1];
    const directionC = [1, 0, -1, 0];
    let nR, nC;
    let distance = -1;
    while (queue.length > 0) {
        while (queue.length > 0) {
            const [cR, cC] = queue.pop();
            grid[cR][cC] = 2;
            for (let d = 0; d < 4; d += 1) {
                nR = cR + directionR[d];
                nC = cC + directionC[d];
                if (0 <= nR && nR < maxR && 0 <= nC && nC < maxC && grid[nR][nC] === 0) {
                    nextQueue.push([nR, nC]);
                    grid[nR][nC] = 2;
                }
            }
        }
        queue = nextQueue;
        nextQueue = [];
        if (queue.length > 0) {
            distance += 1;
        }
    }
    return distance === -1 ? distance : distance + 1;
};
