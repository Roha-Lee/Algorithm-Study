/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;
    let mid;
    let result = 0;
    while(left <= right) {
        mid = Math.floor((left + right) / 2);
        if(nums[mid] < target) {
            left = mid + 1;
            result = left;
        }
        else if(nums[mid] > target) {
            right = mid - 1;
        }
        else {
            return mid;
        }
    }
    return result;
};
