/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var checkPossibility = function(nums) {
  let maxNum = -100000;
  let minNum = 100000;
  let countFromFront = 0;
  let countFromBack = 0;
  for (let i = 0; i < nums.length; i += 1) {
      if (nums[i] < maxNum) countFromFront += 1;
      else maxNum = nums[i];
  }
  for (i = nums.length-1; i >= 0 ; i -= 1) {
      if (nums[i] > minNum) countFromBack += 1;
      else minNum = nums[i];
  }
  return Math.min(countFromFront, countFromBack) <= 1;
};