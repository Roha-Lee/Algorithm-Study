/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    const location = new Map();
    for (let i = 0; i < nums.length; i += 1) {
        const pairLocation = location.get(target - nums[i]);
        if (Number.isInteger(pairLocation)) return [i, pairLocation];
        location.set(nums[i], i);
    }
};