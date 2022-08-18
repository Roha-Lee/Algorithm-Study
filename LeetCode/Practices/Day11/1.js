/**
 * @param {number[]} cost
 * @return {number}
 */
 var minCostClimbingStairs = function(cost) {
    let two_step = cost[0];
    let one_step = cost[1];
    let temp;
    for(let i = 2; i < cost.length; i += 1) {
        temp = one_step;
        one_step = Math.min(one_step, two_step) + cost[i];
        two_step = temp;
    }
    return Math.min(one_step, two_step);
};