// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    const DP = new Array(A.length);
    DP[0] = A[0];
    for(let i = 1; i < A.length; i++){
        let curr = -Infinity;
        for(let j = -6; j < 0; j++){
            if(i+j < 0) continue;
            curr = Math.max(curr, DP[i+j] + A[i]);
        }
        DP[i] = curr;
    }
    return DP[DP.length-1];
}
