function solution(A, K) {
    // write your code in JavaScript (Node.js 8.9.4)
    K = K % A.length;
    return [...A.slice(A.length - K, A.length), ...A.slice(0, A.length - K)];
}