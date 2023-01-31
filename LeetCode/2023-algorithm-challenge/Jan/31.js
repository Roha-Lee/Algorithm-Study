/**
 * @param {number[]} scores
 * @param {number[]} ages
 * @return {number}
 */
var bestTeamScore = function(scores, ages) {
    const pair = [];
    const maxScoreUptoNow = new Array(scores.length).fill(0);
    
    for (let i = 0; i < scores.length; i += 1) {
        pair.push([ages[i], scores[i]]);
    }
    
    pair.sort((a, b) => a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]);
    
    for (let i = 0; i < scores.length; i += 1) {
        maxScoreUptoNow[i] = pair[i][1];
        for (let j = 0; j < i; j += 1) {
            if (pair[j][1] <= pair[i][1]) {
                maxScoreUptoNow[i] = Math.max(maxScoreUptoNow[j] + pair[i][1], maxScoreUptoNow[i])
            } else if (pair[j][0] === pair[i][0]) {
                maxScoreUptoNow[i] = Math.max(maxScoreUptoNow[j] + pair[i][1], maxScoreUptoNow[i]);
            }
        }
    }
    return Math.max(...maxScoreUptoNow);
};
