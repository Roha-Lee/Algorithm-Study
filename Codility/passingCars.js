// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    const prefix = new Array(A.length + 1).fill(0);
    for(let i = A.length-1; i>=0; i--){
        prefix[i] = prefix[i+1] + A[i];
    }
    const result = A.reduce((prev, curr, index) => {
        return prev + (curr === 1 ? 0 : prefix[index]);
    }, 0);
    return result > 1000000000 ? -1 : result;
}
