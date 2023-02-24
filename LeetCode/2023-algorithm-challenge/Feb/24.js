/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumDeviation = function(nums) { 
    const maxPQ = new MaxPriorityQueue();
    for (let i = 0; i < nums.length; i += 1) {
        maxPQ.enqueue(nums[i] % 2 === 0 ? nums[i] : nums[i] * 2);
    }
    let deviation = maxPQ.front().element - maxPQ.back().element;
    while (maxPQ.front().element % 2 === 0) {
        maxPQ.enqueue(maxPQ.dequeue().element / 2);
        deviation = Math.min(deviation, maxPQ.front().element - maxPQ.back().element);
    }
    return deviation;
};
