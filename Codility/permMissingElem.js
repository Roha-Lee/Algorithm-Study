function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    const sumAll = (A.length + 1) * (A.length + 2) / 2;
    const sum = A.reduce((prev, curr) => {
        return prev + curr;
    }, 0)
    return Math.round(sumAll - sum)
}