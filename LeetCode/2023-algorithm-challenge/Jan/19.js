/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraysDivByK = function(nums, k) {
    const prefixSum = getPrefixSumArray(nums);
    const prefixSumModuloCounter = prefixSum.reduce((acc, cur) => {
        let mod = cur % k;
        mod = mod < 0 ? mod + k : mod;
        if (acc.hasOwnProperty(mod)) {
            acc[mod] += 1;
        } else {
            acc[mod] = 1;
        }
        return acc;
    }, {});
    return (
        (prefixSumModuloCounter[0] ?? 0) + 
        Object.values(prefixSumModuloCounter).reduce((acc, cur) => cur > 1 ? acc + (cur * (cur - 1)) / 2 : acc, 0)
    );
};

const getPrefixSumArray = (array) => {
    return array.reduce((acc, cur) => {
        if (acc.length) {
            acc.push(acc[acc.length - 1] + cur);
            return acc;
        }
        return [cur];
    }, []);
}
