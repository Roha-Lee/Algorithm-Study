/**
 * @param {string[]} words
 */
 const WordFilter = function(words) {
    this.prefixMap = new Map();
    this.suffixMap = new Map();
    this.wordToIndex = new Map();
    words.forEach((word, index) => {
        if (this.wordToIndex.has(word)) {
            this.wordToIndex.set(word, index);
            return;
        }
        let wordMap;
        let currMap = this.prefixMap;
        for (let letter of word+"#") {
            wordMap = currMap.get(letter) ?? new Map();
            if (letter === "#") wordMap.set(word, "");
            currMap.set(letter, wordMap);
            currMap = wordMap;
        }
        
        currMap = this.suffixMap;
        for (let letter of word.split("").reverse().join("")+"#") {
            wordMap = currMap.get(letter) ?? new Map();
            if (letter === "#") wordMap.set(word, "");
            currMap.set(letter, wordMap);
            currMap = wordMap;
        }
        this.wordToIndex.set(word, index);
    });
};

/** 
 * @param {string} prefix 
 * @param {string} suffix
 * @return {number}
 */
WordFilter.prototype.f = function(prefix, suffix) {
    let prefixCurr = this.prefixMap;
    let suffixCurr = this.suffixMap;
    let wordMap;
    let hasWordWithPrefix = true;
    let hasWordWithSuffix = true;
    for (let letter of prefix) {
        const wordMap = prefixCurr.get(letter);
        if (!wordMap) {
            hasWordWithPrefix = false;
            break;
        }
        prefixCurr = wordMap;
    }
    
    for (let letter of suffix.split("").reverse().join("")) {
        const wordMap = suffixCurr.get(letter);
        if (!wordMap) {
            hasWordWithSuffix = false;
            break;
        }
        suffixCurr = wordMap;
    }
    if (hasWordWithPrefix && hasWordWithSuffix) {
        const prefixIndices = new Set();
        const suffixIndices = new Set();
        this.gatherAllWordsIndices(prefixCurr, "", prefixIndices);
        this.gatherAllWordsIndices(suffixCurr, "", suffixIndices);
        const intersection = [...prefixIndices].filter(x => suffixIndices.has(x));
        return intersection.reduce((prev, curr) => {
            return Math.max(prev, curr);
        }, -1);
    }
    return -1;
};

WordFilter.prototype.gatherAllWordsIndices = function(letters, letter, indices) {
    if (letter === "#") { 
        for (let word of letters.get(letter).keys()) {
            indices.add(this.wordToIndex.get(word));
        }
        return;
    }
    const nextLetters = letter === "" ? letters : letters.get(letter);
    for (let nextLetter of nextLetters.keys()) {
        this.gatherAllWordsIndices(nextLetters, nextLetter, indices);    
    }
}

/** 
 * Your WordFilter object will be instantiated and called as such:
 * var obj = new WordFilter(words)
 * var param_1 = obj.f(prefix,suffix)
 */