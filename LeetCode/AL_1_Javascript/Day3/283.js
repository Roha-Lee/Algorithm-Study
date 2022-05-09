/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
 var moveZeroes = function(nums) {
    let pos = 0;
    let temp;
    for(let i = 0; i < nums.length; i += 1) {
        if(nums[i] === 0) continue;
        temp = nums[i];
        nums[pos++] = temp;
        nums[i] = temp;
    }
    for(; pos < nums.length; pos += 1) {
        nums[pos] = 0;
    }
};