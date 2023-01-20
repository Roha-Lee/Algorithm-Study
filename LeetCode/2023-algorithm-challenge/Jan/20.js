/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var findSubsequences = function(nums) {
    const results = [];
    const temp = [];
    const keySet = new Set();
    const traverse = (index) => {
        for (let i = index; i < nums.length; i += 1) {
            if (temp.length === 0 || temp[temp.length - 1] <= nums[i]) {
                temp.push(nums[i]);
                const key = stringify(temp);
                if (temp.length >= 2 && !keySet.has(key)) {
                    results.push([...temp]);
                    keySet.add(key);
                }        
                traverse(i + 1);
                temp.pop();
            }
        }
    }
    traverse(0);
    return results;
};

const stringify = (arr) => arr.join(";");
