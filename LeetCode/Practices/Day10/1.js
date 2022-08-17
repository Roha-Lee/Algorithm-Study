/**
 * @param {number} n
 * @return {number}
 */
 var fib = function(n) {
    if (n < 2) return n;
    let prev = [0, 1];
    for (let i = 0; i < n - 1; i += 1) {
        prev = [prev[1], prev[0]+prev[1]];
    }
    return prev[1];
};