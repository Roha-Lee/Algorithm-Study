/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var isAnagram = function(s, t) {
    const sCount = {};
    for (let char of s) {
        if (sCount.hasOwnProperty(char)) sCount[char] += 1;
        else sCount[char] = 1;
    }
    for (let char of t) {
        if (sCount.hasOwnProperty(char)) {
            sCount[char] -= 1;
            if (sCount[char] < 0) return false;
        }        
        else {
            return false;
        };
    }
    return Object.values(sCount).reduce((acc, curr) => acc + curr, 0) === 0;
};