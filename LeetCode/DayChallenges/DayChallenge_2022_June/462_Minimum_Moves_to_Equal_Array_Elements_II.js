/**
 * @param {number[]} nums
 * @return {number}
 */
 var minMoves2 = function(nums) {
  nums.sort((a, b) => a < b ? 1 : -1);
  const median = nums[Math.floor(nums.length / 2)];
  return Math.floor(nums.reduce((acc, curr) => {
      return Math.abs(curr - median) + acc;
  }, 0));
};