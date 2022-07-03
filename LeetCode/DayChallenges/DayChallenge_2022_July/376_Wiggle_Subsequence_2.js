/**
 * @param {number[]} nums
 * @return {number}
 */
 var wiggleMaxLength = function(nums) {
  let up = 1;
  let down = 1;
  let prev = nums[0];
  let curr;
  for (let i = 1; i < nums.length; i += 1) {
      curr = nums[i];
      if (curr > prev) up = down + 1;
      else if (curr < prev) down = up + 1;
      prev = curr;
  }
  return Math.max(up, down);
};