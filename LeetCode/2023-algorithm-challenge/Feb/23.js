/**
 * @param {number} k
 * @param {number} w
 * @param {number[]} profits
 * @param {number[]} capital
 * @return {number}
 */
var findMaximizedCapital = function(k, w, profits, capital) {
    let result = w;
    const candidates = [];
    const pool = new MaxPriorityQueue();
    for (let i = 0; i < profits.length; i += 1) {
        candidates.push([capital[i], profits[i]]);
    }
    candidates.sort((a, b) => b[0] - a[0]);
    
    for (let i = 0; i < k; i += 1) {
        while (candidates.length && result >= candidates[candidates.length-1][0]) {
            pool.enqueue(candidates.pop()[1]);
        }
        const currMax = pool.dequeue()
        if (currMax === null) return result;
        result += currMax.element;
    }
    return result;
};
