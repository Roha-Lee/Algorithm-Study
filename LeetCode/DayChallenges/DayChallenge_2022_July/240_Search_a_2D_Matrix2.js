/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
 var searchMatrix = function(matrix, target) {
    let [row, col] = [0, matrix[0].length-1];
    while (0 <= row && row < matrix.length && 0 <= col && col < matrix[0].length) {
        if (matrix[row][col] > target) col--;
        else if (matrix[row][col] < target) row ++;
        else {
            return true;
        }
    }
    return false;
};
