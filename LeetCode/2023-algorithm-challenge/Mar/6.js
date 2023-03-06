/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function(arr, k) {
    let result = 1;
    let pos = 0;
    let remain = k;
    while (remain) {
        if (arr[pos] === result) {
            pos += 1;
        } else {
            remain -= 1;
        }
        result += 1;
    }
    return result - 1;
};
