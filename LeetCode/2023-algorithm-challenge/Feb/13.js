/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(low, high) {
    return (low % 2 === 1 && high % 2 === 1) + Math.ceil((high - low) / 2);
};
