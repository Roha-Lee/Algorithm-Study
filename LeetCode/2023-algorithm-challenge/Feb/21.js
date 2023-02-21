/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function(nums) {
    let left = 0;
    let right = nums.length - 1;
    let mid;
    while (left < right) {
        console.log(left, right);
        mid = Math.floor((right + left) / 2);
        if (mid > 0 && nums[mid] === nums[mid - 1]) {
            if (mid % 2 === 0) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else if (mid + 1 < nums.length && nums[mid] === nums[mid + 1]) {
            if (mid % 2 === 0) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        } else {
            return nums[mid];
        }
    }
    return nums[left];
};
