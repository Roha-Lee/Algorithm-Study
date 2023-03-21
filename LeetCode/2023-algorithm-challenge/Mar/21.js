/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function(nums) {
    nums.push('#');
    let result = 0;
    let count = 0;
    for (let num of nums) {
        if (num === 0) {
            count += 1;
        } else {
            result += count * (count + 1) / 2;
            count = 0;
        }
    }
    return result;
};
