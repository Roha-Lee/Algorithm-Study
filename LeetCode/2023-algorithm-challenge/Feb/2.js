/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function(words, order) {
    const letterMap = {};
    const alphabets = "abcdefghijklmnopqrstuvwxyz";
    for(let i = 0; i < order.length; i += 1) {
        letterMap[order[i]] = alphabets[i];
    }
    const convertedWords = words.map((word) => Array.from(word).map(letter => letterMap[letter]).join(""));
    const sortedWords = [...convertedWords];
    sortedWords.sort();

    for (let i = 0; i < convertedWords.length; i += 1) {
        if (sortedWords[i] !== convertedWords[i]) {
            return false;
        }
    }
    return true;
};
