/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var isAnagram = function(s, t) {
    const info = new Map();
    let count;
    let letter;
    Array.from(s).forEach(letter => {
        count = info.get(letter);
        if(count) {
            info.set(letter, count + 1);
        }
        else {
            info.set(letter, 1);
        }
    });
    for(let i = 0; i < t.length; i += 1) {
        letter = t[i];
        count = info.get(letter);
        if(count === undefined || count <= 0) {
            return false;
        }
        info.set(letter, count - 1);
    }
    for(const [key, value] of info) {
        if(value > 0) return false;
    }
    return true;
};