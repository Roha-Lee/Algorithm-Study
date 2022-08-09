/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var isIsomorphic = function(s, t) {
    const letters1 = {};
    const letters2 = {};
    let charS;
    let charT
    for (let i = 0; i < s.length; i += 1) {
        charS = s[i];
        charT = t[i];
        if (!letters1[charS]) {
            letters1[charS] = charT;
        }
        if (letters1[charS] && letters1[charS] !== charT) return false;
        if (!letters2[charT]) {
            letters2[charT] = charS;
        }
        if (letters2[charT] && letters2[charT] !== charS) return false;
    }
    return true;
};