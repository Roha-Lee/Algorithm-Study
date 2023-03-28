/**
 * @param {number[]} days
 * @param {number[]} costs
 * @return {number}
 */
var mincostTickets = function(days, costs) {
    const dp = new Array(days[days.length - 1] + 1).fill(0);
    for (let i = 1; i < dp.length; i += 1) {
        if (!days.includes(i)) {
            dp[i] = dp[i-1];
        } else {
            const day1Cost = dp[i-1] + costs[0];
            const day7Start = Math.max(0, i - 7);
            let j = i-1;
            while (j >= 0 && days[j] >= days[i] - 6) {
                j -= 1;
            }
            const day7Cost = dp[day7Start] + costs[1];
            const day30Start = Math.max(0, i - 30);
            j = i-1;
            while (j >= 0 && days[j] >= days[i] - 29) {
                j -= 1;
            }
            const day30Cost = dp[day30Start] + costs[2];
            dp[i] = Math.min(day1Cost, day7Cost, day30Cost);
        }
    }
    return dp[dp.length - 1];
};
