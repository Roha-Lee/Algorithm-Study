/**
 * @param {number} n
 * @param {number} k
 * @param {number} target
 * @return {number}
 */
 var numRollsToTarget = function (d, f, target) {
    const dp = Array.from(Array(d + 1), () => Array(target + 1).fill(0));
    let mod = 1000000007;
    for (let j = 1; j <= f; j++) {
        if (j <= target) {
            dp[1][j] = 1;
        }
    }
    for (let i = 2; i <= d; i++) {
        for (let j = 1; j < target + 1; j++) {
            k = 1;
            for (let k = 1; k <= f; k++) {
                if (j - k > 0) {
                    dp[i][j] += dp[i - 1][j - k];
                }
            }
            dp[i][j] %= mod;
        }
    }
    return dp[d][target];
};