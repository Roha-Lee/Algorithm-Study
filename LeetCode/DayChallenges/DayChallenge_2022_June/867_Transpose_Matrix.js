/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
 var transpose = function(matrix) {
    const numRow = matrix.length;
    const numCol = matrix[0].length;
    const returnArray = Array.from(Array(numCol), () => new Array(numRow));
    for(let r = 0; r < numRow; r +=1 ) {
        for(let c = 0; c < numCol; c += 1) {
            returnArray[c][r] = matrix[r][c];
        }
    }
    return returnArray;
};