/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var countSmaller = function(nums) {
    const used = [];
    const result = [];
    const reversed = nums.reverse();
    for(let elem of reversed) {
        const idx = binarySearch(used, elem, 0, used.length);
        result.push(idx);
        used.splice(idx, 0, elem);
    }
    return result.reverse();
};
var binarySearch = function(nums, num, left, right) {
    let mid;
    while (left < right) {
        mid = Math.floor((left + right) / 2);
        if (nums[mid] >= num) {
            right = mid;
        }
        else {
            left = mid + 1;
        }
    }
    return left;
}