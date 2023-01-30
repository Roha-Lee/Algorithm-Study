/**
 * @param {number} n
 * @return {number}
 */
var tribonacci = function(n) {
    const DP = new Array(38);
    DP[0] = 0;
    DP[1] = 1;
    DP[2] = 1;
    for (let i = 3; i <= n; i += 1) {
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3];
    }
    return DP[n];
};
