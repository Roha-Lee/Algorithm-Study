/**
 * @param {number[]} nums
 * @return {number}
 */
 var rob = function(nums) {
    if (nums.length <= 1) return nums[0];
    const dp = new Array(nums.length).fill(0);
    dp[0] = nums[0];
    dp[1] = Math.max(nums[1], dp[0]);
    for (let i = 2; i < nums.length; i += 1) {
        dp[i] = Math.max(dp[i-1], nums[i] + dp[i-2]);
    }
    return dp.pop();
};