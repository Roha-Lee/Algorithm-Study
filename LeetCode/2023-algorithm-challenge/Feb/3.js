/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    if (numRows === 1) {
        return s;
    }
    const rows = new Array(numRows).fill("");
    let index = 0;
    let direction;
    for (let i = 0; i < s.length; i += 1) {
        if (index === 0) {
            direction = 1;
        } else if (index === (numRows - 1)) {
            direction = -1;
        }
        rows[index] += s[i];
        index += direction;
    }
    return rows.join("");
};
