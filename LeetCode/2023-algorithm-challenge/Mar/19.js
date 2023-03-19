var WordDictionary = function() {
    this.trie = {};
};

/** 
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {
    let curr = this.trie;
    for (let i = 0, len = word.length; i < len; i += 1) {
        if (!curr.hasOwnProperty(word[i])) {
            curr[word[i]] = {};
        }
        curr = curr[word[i]];
    }
    curr["#"] = word;
};

/** 
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function(word) {
    word = word + "#";
    let queue = [];
    let nextQueue = [this.trie];
    for (let i = 0, len = word.length; i < len; i += 1) {
        queue = nextQueue;
        nextQueue = [];
        while (queue.length) {
            
            const curr = queue.pop();
            if (word[i] === ".") {
                Object.keys(curr).forEach(key => {
                    if (key === "#") return;
                    nextQueue.push(curr[key])
                });
            } else {
                if (curr.hasOwnProperty(word[i])) {
                    nextQueue.push(curr[word[i]]);
                }
            }
            
        }
        if (nextQueue.length === 0) {
            return false;
        }
    }
    return true;
};

/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */
