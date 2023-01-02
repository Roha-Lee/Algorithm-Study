/**
 * @param {string} word
 * @return {boolean}
 */
var detectCapitalUse = function(word) {
    const letters = word.split("");
    const allCapital = letters.every(letter => letter.charCodeAt() <= "Z".charCodeAt());
    const allLower = letters.every(letter => letter.charCodeAt() >= "a".charCodeAt());
    const capitalized = letters[0].charCodeAt() <= "Z".charCodeAt() && letters.slice(1).every(letter => letter.charCodeAt() >= "a".charCodeAt());
    return allCapital || allLower || capitalized;
};