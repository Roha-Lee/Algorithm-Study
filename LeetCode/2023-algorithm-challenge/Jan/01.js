/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
var wordPattern = function(pattern, s) {
    const words = s.split(' ');
    if (words.length !== pattern.length) {
        return false;
    }
    const wordToPattern = {};
    const patternToWord = {};
    for (let i = 0; i < pattern.length; i += 1) {
        const currPattern = pattern[i];
        const currWord = words[i];
        if (patternToWord.hasOwnProperty(currPattern)) {
            if (patternToWord[currPattern] !== currWord) {
                return false;
            }
        } else if (wordToPattern.hasOwnProperty(currWord)) {
            return false;
        } else {
            patternToWord[currPattern] = currWord;
            wordToPattern[currWord] = currPattern;
        }
    }
    return true;
};