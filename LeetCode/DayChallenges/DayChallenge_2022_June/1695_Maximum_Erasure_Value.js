/**
 * @param {number[]} nums
 * @return {number}
 */
 var maximumUniqueSubarray = function(nums) {
    let maxScore = 0;
    let left = 0;
    let currScore = 0;
    const numSet = new Set();
    for (let right = 0; right < nums.length; right += 1) {
        while (numSet.has(nums[right])) {
            currScore -= nums[left];
            numSet.delete(nums[left]);
            left += 1;
        }
        currScore += nums[right];
        numSet.add(nums[right]);
        maxScore = Math.max(currScore, maxScore);
    }
    return maxScore;
};