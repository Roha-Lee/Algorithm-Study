/**
 * @param {string[]} words
 * @return {number}
 */
 var longestStrChain = function(words) {
    const wordsMap = new Map();
    const dp = new Map();
    for(let word of words) {
        if (!wordsMap.get(word.length)) {
            wordsMap.set(word.length, new Set());    
        }
        wordsMap.get(word.length).add(word);
        dp.set(word, 1);
    }
    
    let targetWord;
    let currChain;
    let maxChain = 0;
    for (let len = 1; len <= 16; len += 1) {
        wordsMap.get(len)?.forEach( (word) => {
            for (let i = 0; i < len; i += 1) {
                targetWord = word.substr(0, i) + word.substr(i+1);
                currChain = (dp.get(targetWord) ?? 0) + 1;
                dp.set(word, Math.max(currChain, dp.get(word)));
                maxChain = Math.max(maxChain, currChain);
            }
        });
    }
    return maxChain;
};