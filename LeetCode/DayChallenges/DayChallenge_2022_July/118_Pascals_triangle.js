/**
 * @param {number} numRows
 * @return {number[][]}
 */
 var generate = function(numRows) {
    if(numRows === 1) return [[1]];
    const result = [[1], [1,1]];
    if(numRows === 2) return result;
    for(let i = 2; i < numRows; i += 1) {
        const temp = [1];
        for(let j = 1; j < result[i-1].length; j += 1) {
            temp.push(result[i-1][j] + result[i-1][j-1]);
        }
        temp.push(1);
        result.push(temp);
    }
    return result;
};