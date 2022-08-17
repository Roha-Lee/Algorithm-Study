/**
 * @param {number} n
 * @return {number}
 */
// var climbStairs = function(n) {
//     const steps = new Array(n+1).fill(1);
//     for (let i = 2; i <= n; i += 1) {
//         steps[i] = steps[i-1] + steps[i-2];
//     }
//     return steps[n];
// };

// var climbStairs = function(n) {
//     if (n === 1) return n;
//     let prev = [1, 1];
//     for (let i = 2; i <= n; i += 1) {
//         prev = [prev[1], prev[0] + prev[1]];
//     }
//     return prev[1];
// };

var climbStairs = function(n) {
    if (n === 1) return n;
    let first = 1; 
    let second = 1; 
    let temp;
    for (let i = 2; i <= n; i += 1) {
        temp = second;
        second = first + second;
        first = temp;   
    }
    return second;
};