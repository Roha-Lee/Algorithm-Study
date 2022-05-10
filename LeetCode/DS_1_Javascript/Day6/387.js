/**
 * @param {string} s
 * @return {number}
 */
 var firstUniqChar = function(s) {
    const info = new Map();
    let result = Infinity;
    Array.from(s).forEach((letter, index) => {
        if(info.has(letter)) {
            let [loc, freq] = info.get(letter);
            info.set(letter, [loc, freq + 1]);
        }
        else {
            info.set(letter, [index, 1]);
        }
    });
    for(const [key, [loc, freq]] of info) {
        if(freq > 1) continue;
        result = Math.min(result, loc);
    }
    if(result === Infinity) return -1;
    return result;
};