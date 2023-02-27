/**
 * // Definition for a QuadTree node.
 * function Node(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight) {
 *    this.val = val;
 *    this.isLeaf = isLeaf;
 *    this.topLeft = topLeft;
 *    this.topRight = topRight;
 *    this.bottomLeft = bottomLeft;
 *    this.bottomRight = bottomRight;
 * };
 */

/**
 * @param {number[][]} grid
 * @return {Node}
 */
var construct = function(grid) {
    const quadTree = (grid, size, startRow, startCol) => {    
        const half = size / 2;
        const isLeaf = allSame(grid, size, startRow, startCol);
        if (isLeaf || half < 1) {
            return new Node(grid[startRow][startCol], true, null, null, null, null);
        } else {
            const topLeft = quadTree(grid, half, startRow, startCol);
            const topRight = quadTree(grid, half, startRow, startCol + half);
            const bottomLeft = quadTree(grid, half, startRow + half, startCol);
            const bottomRight = quadTree(grid, half, startRow + half, startCol + half);
            return new Node(
                grid[startRow][startCol],
                isLeaf,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight,
            );
        }
    };
    return quadTree(grid, grid.length, 0, 0);
};

const allSame = (grid, size, startRow, startCol) => { 
    const element = grid[startRow][startCol];
    for (let row = startRow; row < startRow + size; row += 1) {
        for (let col = startCol; col < startCol + size; col += 1) {
            if (grid[row][col] !== element) {
                return 0;
            }
        }
    }
    return 1;
};
