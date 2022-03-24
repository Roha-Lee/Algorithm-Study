// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    A = A.filter(item => item > 0);
    const hashTable = new Set([...A]);
    for(let i = 1; i <= 100001; i++){
        if(!hashTable.has(i)){
            return i;
        }
    }
}
