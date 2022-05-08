/**
 * @param {number[]} nums
 * @return {number}
 */
 var maxSubArray = function(nums) {
    const sums = new Array(nums.length);
    nums.forEach((num, index) => {
        if(index === 0){
            sums[index] = nums[index];
        }
        else{
            sums[index] = Math.max(sums[index - 1] + num, num);    
        }
    })
    return sums.reduce((prev, curr) => {
        return Math.max(prev, curr);
    })
};