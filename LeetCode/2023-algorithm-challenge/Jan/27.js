/**
 * @param {string[]} words
 * @return {string[]}
 */
var findAllConcatenatedWordsInADict = function(words) {
    const concatenatedWords = [];
    const wordsSet = new Set();
    words.sort((a, b) => a.length - b.length);
    const isConcatenateWord = (word) => {
        for (let i = 1; i <= word.length; i += 1) {
            const prefix = word.slice(0, i);
            const suffix = word.slice(i);
            if (wordsSet.has(prefix) && (wordsSet.has(suffix) || isConcatenateWord(suffix))) {
                wordsSet.add(suffix);
                return true;
            }
        }
        return false;
    }
    for (let word of words) {
        if (isConcatenateWord(word)) {
            concatenatedWords.push(word); 
        } else {
            wordsSet.add(word);
        }
    }
    return concatenatedWords;
};
