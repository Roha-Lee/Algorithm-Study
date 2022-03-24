// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    const hashTable = new Set([...A]);
    for(let i = 1; i <= A.length; i++){
        if(!hashTable.delete(i)) return 0;
    }
    return 1;
}
