var pivotIndex = function(nums) {
    let sum = 0;
    const totalSum = nums.reduce((acc, curr) => acc + curr, 0);
    for (let i = 0; i < nums.length; i += 1) {
        if (sum === totalSum - nums[i] - sum) {
            return i;
        }
        sum += nums[i];
    }
    return -1;
};