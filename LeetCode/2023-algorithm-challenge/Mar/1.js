/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
    if (nums.length <= 1) {
        return [...nums];
    }
    const mid = Math.floor(nums.length / 2);
    const left = sortArray(nums.slice(0, mid));
    const right = sortArray(nums.slice(mid));
    return merge(left, right);
};

const merge = (left, right) => {
    let leftidx = 0;
    let rightidx = 0;
    const result = [];
    while (leftidx < left.length && rightidx < right.length) {
        if (left[leftidx] < right[rightidx]) {
            result.push(left[leftidx]);
            leftidx += 1;
        } else {
            result.push(right[rightidx]);
            rightidx += 1;
        }
    }
    while (leftidx < left.length) {
        result.push(left[leftidx]);
        leftidx += 1;
    }
    while (rightidx < right.length) {
        result.push(right[rightidx]);
        rightidx += 1;
    }
    return result;
};
