/**
 * @param {number[][]} grid
 * @return {number}
 */
 var maxAreaOfIsland = function(grid) {
    const calcArea = function(grid, r, c) {
        if (grid[r][c] === 0) return;
        grid[r][c] = 0;
        area += 1;
        const dStep = [[0, 1], [1, 0], [0, -1], [-1, 0]];
        for (const [dr, dc] of dStep) {
            const [nr, nc] = [r + dr, c + dc];
            if (0 <= nr && nr < rows && 0 <= nc && nc < cols && grid[nr][nc] == 1) {
                calcArea(grid, nr, nc);
            }
        }
    }      
    let maxArea = 0;
    let area = 0;
    const rows = grid.length;
    const cols = grid[0].length;

    for (let r = 0; r < rows; r += 1) {
        for (let c = 0; c < cols; c += 1) {
            if (grid[r][c] === 1) {
                calcArea(grid, r, c);
                maxArea = Math.max(area, maxArea);
                area = 0;
            }
        }
    }
    return maxArea;
};

