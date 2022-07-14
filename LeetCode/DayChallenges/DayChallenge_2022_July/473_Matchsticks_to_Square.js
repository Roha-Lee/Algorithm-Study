/**
 * @param {number[]} matchsticks
 * @return {boolean}
 */
 var makesquare = function(nums) {
  var sum = nums.reduce((a, b) => a + b, 0);
  if (sum === 0 || sum % 4 !== 0) {
      return false;
  }
  
  var seen = new Array(nums.length);
  var canPartition = function(start, blocks, sum, target) {
      if (blocks === 1) {
          return true;
      }
      
      if (sum === target) {
          return canPartition(0, blocks - 1, 0, target);
      } else if (sum > target) {
          return false;
      }
      
      for (var i = start; i < nums.length; i++) {
          if (!seen[i]) {
              seen[i] = true;
              if (canPartition(i + 1, blocks, sum + nums[i], target)) {
                  return true;
              }
              seen[i] = false;
          }
      }
      return false;
  }
          
  return canPartition(0, 4, 0, sum / 4);
};