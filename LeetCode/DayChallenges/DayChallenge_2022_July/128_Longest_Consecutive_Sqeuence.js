/**
 * @param {number[]} nums
 * @return {number}
 */
 var longestConsecutive = function(nums) {
  let set = new Set(nums);
  let c = 0, length = 0;
  for (let num of nums) {
      if (!set.has(num-1)){
          let temp = num;
          while (set.has(temp++)) {
              c++;
              length = Math.max(length, c);
          }
          c = 0;
      }
  }
  return length;
};