/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var search = function(nums, target) {
    let result = -1;
    var helper = function(left, right) {
        if (left > right) return;
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] < target) helper(left + 1, right);
        else if (nums[mid] > target) helper(left, right - 1);
        else result = mid;
    }
    helper(0, nums.length - 1);
    return result;
};