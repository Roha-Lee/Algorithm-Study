/**
 * @param {string} s1
 * @return {Map}
 */
 const makeLetterMap = function(s) {
    const map = new Map();
    Array.from(s).forEach(letter => {
        if(map.has(letter)) {
            map.set(letter, map.get(letter) + 1);
        }
        else {
            map.set(letter, 1);
        }
    });
    return map;
}

/**
 * @param {Map} m1
 * @param {Map} m2
 * @return {boolean}
 */
const isSameMap = function(m1, m2) {
    for(const [key, value] of m1) {
        if(!m2.has(key) || m2.get(key) !== value) return false;  
    }
    return true;
}

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    const letters = makeLetterMap(s1);
    const candidate = makeLetterMap(s2.slice(0, s1.length));
    const len = s1.length;
    if(isSameMap(letters, candidate)) return true;
    for(let i = len; i < s2.length; i += 1) {
        const addLetter = s2[i];
        const removeLetter = s2[i-len];
        candidate.set(removeLetter, candidate.get(removeLetter) - 1);
        if(candidate.has(addLetter)) {
            candidate.set(addLetter, candidate.get(addLetter) + 1);
        }
        else {
            candidate.set(addLetter, 1);
        }
        if(isSameMap(letters, candidate)) return true;
    }
    return false;
};