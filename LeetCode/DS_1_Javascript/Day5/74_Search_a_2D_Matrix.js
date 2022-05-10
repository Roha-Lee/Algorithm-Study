/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
 var searchMatrix = function(matrix, target) {
    const rows = matrix.length;
    const cols = matrix[0].length;
    let left = 0;
    let right = rows * cols - 1;
    let mid;
    let row; 
    let col;
    let curr;
    while(left <= right) {
        mid = Math.floor((left + right) / 2);
        row = Math.floor(mid / cols);
        col = mid % cols;
        curr = matrix[row][col];
        if(curr < target) left = mid + 1;
        else if(curr > target) right = mid - 1;
        else return true;
    }
    return false;
};