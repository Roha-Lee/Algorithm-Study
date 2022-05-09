/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    const rearrange = new Array(nums);
    let front = 0;
    let rear = nums.length - 1;
    let pos = nums.length - 1;
    while (front <= rear){
        if(Math.abs(nums[front]) < Math.abs(nums[rear])) {
            rearrange[pos--] = nums[rear--];
        }
        else {
            rearrange[pos--] = nums[front++];
        }
    }
    return rearrange.map(x => x*x);
};