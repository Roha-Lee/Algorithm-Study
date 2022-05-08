/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    const remainders = new Map();
    const result = [];
    nums.forEach((num, index) => {
        if (remainders.has(num)) {
            result.push(remainders.get(num));
            result.push(index);
        }
        remainders.set(target - num, index);    
    }); 
    return result;
};