/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var runningSum = function(nums) {
    let sums = 0;
    const result = [];
    for (let num of nums) {
        sums += num;
        result.push(sums);
    }
    return result;
};