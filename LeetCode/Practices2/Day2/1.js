/**
 * @param {string[]} strs
 * @return {string}
 */
 var longestCommonPrefix = function(strs) {
    const shortest = Math.min(...strs.map(v => v.length));
    for (let i = 0; i < shortest; i += 1) {
        if (strs.some(v => v[i] !== strs[0][i])) return strs[0].slice(0, i);
    }
    return strs[0].slice(0, shortest);
};