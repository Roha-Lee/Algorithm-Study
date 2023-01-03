/**
 * @param {string[]} strs
 * @return {number}
 */
var minDeletionSize = function(strs) {
    let result = 0;
    for (let c = 0; c < strs[0].length; c += 1) {
        for (let r = 0; r < strs.length - 1; r += 1) {
            if (strs[r+1][c].charCodeAt() - strs[r][c].charCodeAt() < 0) {
                result += 1;
                break;
            }
        }
    }
    return result;
};