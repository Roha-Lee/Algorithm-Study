/**
 * @param {number[][]} matrix
 */
 var NumMatrix = function(matrix) {
    const numRow = matrix.length;
    const numCol = matrix[0].length;
    this.prefixSumMatrix = Array.from(Array(numRow), () => new Array(numCol));
    this.prefixSumMatrix[0][0] = matrix[0][0];
    for(let r = 1; r < numRow; r += 1) {
        this.prefixSumMatrix[r][0] = this.prefixSumMatrix[r-1][0] + matrix[r][0];
    }
    for(let c = 1; c < numCol; c += 1) {
        this.prefixSumMatrix[0][c] = this.prefixSumMatrix[0][c-1] + matrix[0][c];
    }
    for(let r = 1; r < numRow; r += 1) {
        for(let c = 1; c < numCol; c += 1) {
            this.prefixSumMatrix[r][c] = 
                this.prefixSumMatrix[r][c-1] + 
                this.prefixSumMatrix[r-1][c] -
                this.prefixSumMatrix[r-1][c-1] +
                matrix[r][c];
        }
    }
    
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
    const bottomRight = this.prefixSumMatrix[row2][col2];
    const bottomLeft = col1 === 0 ? 0 : this.prefixSumMatrix[row2][col1-1];
    const topRight = row1 === 0 ? 0 : this.prefixSumMatrix[row1-1][col2];
    const topLeft = (row1 === 0 || col1 === 0) ? 0 : this.prefixSumMatrix[row1-1][col1-1];
    return bottomRight - bottomLeft - topRight + topLeft;
};

/** 
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */