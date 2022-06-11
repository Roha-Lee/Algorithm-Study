/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
 var minOperations = function(nums, x) {
    const sum = nums.reduce((prev, curr) => {return prev + curr}, 0);
    const target = sum - x;
    let left = 0;
    let currentSum = 0;
    let maxLength = -1;
    for (let right = 0; right < nums.length; right += 1) {
        currentSum += nums[right];
        while (target < currentSum) currentSum -= nums[left++];
        if (target === currentSum) maxLength = Math.max(maxLength, right - left + 1);
    }
    return maxLength === -1 ? -1 : nums.length - maxLength;
};