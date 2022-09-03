/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
 var coinChange = function(coins, amount) {
    const dp = new Array(amount + 1).fill(Infinity);
    let next;
    dp[0] = 0;
    for (let value of coins) {
        for (let remain = value; remain < amount + 1; remain += 1) {
            next = remain - value;
            if (next >= 0) {
                dp[remain] = Math.min(1 + dp[next], dp[remain]);
            }    
        }        
    }
    return dp[dp.length-1] === Infinity ? -1 : dp[dp.length-1];
};