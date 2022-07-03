/**
 * @param {number[]} nums
 * @return {number}
 */
 var wiggleMaxLength = function(nums) {
  const diff = [];
  let maxLength = 1;
  nums.reduce((acc, curr) => {
      diff.push(curr - acc);
      return curr;
  }, nums[0]);
  diff.reduce((acc, curr) => {
      if (curr === 0) return acc;
      if (acc === 0) {
          maxLength += 1;
          return curr;
      }
      maxLength += Number((acc > 0) === (curr < 0));    
      return curr;
  }, 0);
  return maxLength;
};