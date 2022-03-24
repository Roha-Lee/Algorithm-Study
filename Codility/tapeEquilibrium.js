// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    const prefixSum = [];
    const sumA = A.reduce((prev, curr) => {
        prefixSum.push(prev);
        return prev + curr;
    });
    return prefixSum.reduce((prev, curr) => {
        return Math.min(prev, Math.abs(sumA - 2 * curr));
    }, 1000000000)
}
