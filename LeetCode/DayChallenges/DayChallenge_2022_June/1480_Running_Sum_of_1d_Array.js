/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var runningSum = function(nums) {
    sums = [nums[0]];
    for(let i = 1; i < nums.length; i += 1) {
        sums.push(sums[sums.length - 1] + nums[i]);
    }
    return sums;
};