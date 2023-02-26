/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
var minDistance = function(word1, word2) {
    let memo = new Array(word2.length + 1).fill(0)
    for (let index1 = word1.length; index1 >= 0; index1--) {
        const current = new Array(word2.length + 1).fill(0)
        for (let index2 = word2.length; index2 >= 0; index2--) {
            const a = word1[index1]
            const b = word2[index2]
            if (index1 === word1.length) {
                current[index2] = word2.length - index2
            } else if (index2 === word2.length) {
                current[index2] = word1.length - index1
            } else if (a === b) {
                current[index2] += memo[index2 + 1]
            } else {
                current[index2] += Math.min(
                memo[index2],
                current[index2 + 1],
                memo[index2 + 1],
                ) + 1
            }
        }
        memo = current;
    }
    return memo[0];
};
