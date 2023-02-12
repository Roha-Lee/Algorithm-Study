/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */
var nthSuperUglyNumber = function(n, primes) {
    let candidates = [1];
    const factor = new Array(primes.length).fill(0);
    while (candidates.length < n) {
        let nextNumber = Infinity;
        for (let i = 0; i < primes.length; i += 1) {
            const candidate = candidates[factor[i]] * primes[i];
            if (candidate < nextNumber) {
                nextNumber = candidate;
            }
        }
        for (let i = 0; i < factor.length; i += 1) {
            if (candidates[factor[i]] * primes[i] === nextNumber) {
                factor[i] += 1
            }
        }
        candidates.push(nextNumber);
    }
    return candidates[n-1];
};
