/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
 var kInversePairs = function(n, k) { 
    if (n * (n-1) / 2 < k) return 0;
    let maxK;
    let temp;
    let arr;
    let prev = new Array(k+1).fill(0n);
    for (let r = 1 ; r <= n; r += 1) {
        temp = 1n;
        arr = new Array(k+1).fill(0n);
        maxK = r * (r-1) / 2;
        for (let c = 0; c <= Math.min(k, maxK); c += 1) {
            if (c === 0) {
                arr[c] = 1n;
                continue;
            }
            if (c >= r) temp -= prev[c-r];
            temp += prev[c];
            arr[c] = temp;    
        }
        prev = arr;
    }
    
    return arr[k] % 1000000007n;
};