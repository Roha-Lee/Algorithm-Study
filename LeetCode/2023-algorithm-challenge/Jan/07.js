/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    const remains = new Array(gas.length).fill(0);
    const sum = gas.reduce((acc, curr, index) => {
        return acc + curr - cost[index];
    }, 0); 
    if (sum < 0) return -1;
    for (let i = 1; i < gas.length; i += 1) {
        const diff = gas[i-1] - cost[i-1];
        remains[i] = remains[i-1] + diff;
    }
    const minValue = Math.min(...remains);
    return remains.findIndex(remain => remain === minValue);
};
