var Trie = function() {
    this.trie = {};
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let curr = this.trie;
    for (let i = 0, len = word.length; i < len; i += 1) {
        if (!curr.hasOwnProperty(word[i])) {
            curr[word[i]] = {};
        }
        curr = curr[word[i]];
    }
    curr["#"] = "#";
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let curr = this.trie;
    for (let i = 0, len = word.length; i < len; i += 1) {
        curr = curr[word[i]];
        if (curr === undefined) {
            return false;
        }
    }
    return Boolean(curr['#']);
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let curr = this.trie;
    for (let i = 0, len = prefix.length; i < len; i += 1) {
        curr = curr[prefix[i]];
        if (curr === undefined) {
            return false;
        }
    }
    return true;
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
