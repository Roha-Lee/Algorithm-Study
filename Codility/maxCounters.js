// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N, A) {
    // write your code in JavaScript (Node.js 8.9.4)
    const counters = new Array(N).fill(0);
    let maxValue = 0, maxTemp = 0;
    A.forEach(op => {
        if(op !== N + 1){
            counters[op-1] = counters[op-1] >= maxValue ? counters[op-1] + 1 : maxValue + 1;
            maxTemp = Math.max(maxTemp, counters[op-1]);
        }
        else{
            maxValue = maxTemp;
        }
    });
    return counters.map(item => {
        return item > maxValue ? item : maxValue;
    })
}