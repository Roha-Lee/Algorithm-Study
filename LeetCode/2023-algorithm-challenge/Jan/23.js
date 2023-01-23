/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    if (trust.length === 0) {
        return n === 1 ? 1 : -1;
    }
    const forward = {};
    const backward = {};
    for (let [src, dst] of trust) {
        if (backward.hasOwnProperty(dst)) {
            backward[dst].push(src);
        } else {
            backward[dst] = [src];
        }
        if (forward.hasOwnProperty(src)) {
            forward[src].push(dst);
        } else {
            forward[src] = [dst];
        }
    }
    for (let i = 1; i <= n; i += 1) {
        if (!forward[i] && backward[i]?.length === n-1) return i;
    }
    return -1;
};
