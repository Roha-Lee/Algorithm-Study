/**
 * @param {number[]} nums
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
var countSubarrays = function(nums, minK, maxK) {
    let minCheck = false;
    let maxCheck = false;
    let start = 0;
    let minStart = 0;
    let maxStart = 0;
    let count = 0;
    for (let i = 0; i < nums.length; i += 1) {
        const num = nums[i];
        if (num < minK || num > maxK) {
            minCheck = false;
            maxCheck = false;
            start = i + 1;
        }
        if (num === minK) {
            minCheck = true;
            minStart = i;
        }
        if (num === maxK) {
            maxCheck = true;
            maxStart = i;
        }
        if (minCheck && maxCheck) {
            count += (Math.min(minStart, maxStart) - start + 1);
        }
    }
    return count;
};
