/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var searchRange = function(nums, target) {
    return binarySearch(nums, target, 0, nums.length-1);
};

var binarySearch = function(nums, target, left, right) {
    if (!nums.length) return [-1, -1];
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] > target) right = mid - 1;
        else if (nums[mid] < target) left = mid + 1;
        else {
            let rangeLeft = mid;
            let rangeRight = mid;
            while (nums[rangeLeft] === target) rangeLeft--;
            while (nums[rangeRight] === target) rangeRight++;
            return [rangeLeft+1, rangeRight-1];
        }
    }
    return [-1, -1];
}