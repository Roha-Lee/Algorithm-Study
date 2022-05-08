/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function(nums) {
    const nums_set = new Set(nums);
    return nums_set.size !== nums.length;
  };