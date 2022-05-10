/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
 var canConstruct = function(ransomNote, magazine) {
    const counter = new Map();
    Array.from(magazine).forEach(letter => {
        if(counter.has(letter)) {
            counter.set(letter, counter.get(letter) + 1);
        }
        else {
            counter.set(letter, 1);
        }
    });
    for(let i = 0; i < ransomNote.length; i += 1) {
        const count = counter.get(ransomNote[i]);
        if(count === undefined || count <= 0) {
            return false;
        }
        counter.set(ransomNote[i], count - 1);
    }
    return true;
};