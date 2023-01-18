/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubarraySumCircular = function(nums) {
    let sum = nums.reduce((acc, cur) => acc + cur, 0);
    let maxSum = -Infinity
    let tempMaxSum = -Infinity;
    let minSum = Infinity;
    let tempMinSum = Infinity;
    for (let i = 0; i < nums.length; i += 1) {
        tempMaxSum = Math.max(tempMaxSum + nums[i], nums[i]);
        maxSum = Math.max(maxSum, tempMaxSum);
        tempMinSum = Math.min(tempMinSum + nums[i], nums[i]);
        minSum = Math.min(minSum, tempMinSum);
    }
    if (sum === minSum) return maxSum;
    return Math.max(maxSum, sum - minSum);
};
