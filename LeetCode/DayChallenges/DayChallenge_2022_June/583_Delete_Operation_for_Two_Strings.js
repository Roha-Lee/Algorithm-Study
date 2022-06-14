/**
 * @param {string} word1
 * @param {string} word2
 * @return {number}
 */
 var minDistance = function(word1, word2) {
    const n = word1.length;
    const m = word2.length;
    let DP = new Array(n+1).fill(0).map(x => Array(m+1).fill(0));
    for (let i = 1; i < n+1; i+=1) {
        for (let j = 1; j< m+1; j+=1) {
            DP[i][j] = Math.max(DP[i-1][j], DP[i][j-1]);
            if (word1[i-1] === word2[j-1]) {
                DP[i][j] = 1 + DP[i-1][j-1];
            }
        }
    }
    return n + m - 2 * DP[n][m]; 
};