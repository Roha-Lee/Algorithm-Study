function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    return A.reduce((prev, curr) => {
        return prev ^ curr;
    }, 0)
}