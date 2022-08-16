/**
 * @param {character[][]} grid
 * @return {number}
 */
 var numIslands = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    const removeIsland = function(r, c) {
        const moves = [[0, 1], [0, -1], [1, 0], [-1, 0]];
        for (let [dr, dc] of moves) {
            const [nr, nc] = [r + dr, c + dc];
            if (0 > nr || rows <= nr || 0 > nc || cols <= nc) continue;
            if (grid[nr][nc] === "1") {
                grid[nr][nc] = "0";
                removeIsland(nr, nc);
            }

        }    
    }
    let count = 0;
    for (let r = 0; r < rows; r += 1) {
        for (let c = 0; c < cols; c += 1) {
            if (grid[r][c] === "1") {
                grid[r][c] = "0";
                removeIsland(r, c);
                count += 1;
            }
        }
    }
    return count;
};