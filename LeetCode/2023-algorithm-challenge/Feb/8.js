/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    const dp = new Array(nums.length).fill(Infinity);
    dp[0] = 0;
    for (let pos = 1; pos < nums.length; pos += 1) {
        for (let j = 0; j < pos; j += 1) {
            if (j + nums[j] >= pos) {
                dp[pos] = Math.min(dp[pos], dp[j] + 1);
            }
        }
    }
    return dp[dp.length - 1];
};                                                                                   
