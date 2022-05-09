/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
 var matrixReshape = function(mat, r, c) {
    if(mat.length * mat[0].length !== r*c) return mat;
    const result = Array.from(Array(r), () => new Array(c));
    let pos = 0;
    let row; 
    let col;
    mat.forEach(row => {
        row.forEach(num => {
            row = Math.floor(pos / c);
            col = pos % c;
            result[row][col] = num;
            pos += 1;
        });
    });
    return result;
};