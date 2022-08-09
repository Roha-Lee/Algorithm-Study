/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var isSubsequence = function(s, t) {
    if (s.length === 0) return true;
    let idx1 = 0; 
    let idx2 = 0;
    for (let char of t) {
        if (char === s[idx1]) idx1 += 1;
        if (idx1 === s.length) return true;
    }
    return false;
};