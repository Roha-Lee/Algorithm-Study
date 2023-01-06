/**
 * @param {number[]} costs
 * @param {number} coins
 * @return {number}
 */
var maxIceCream = function(costs, coins) {
    costs.sort((a, b) => a - b);
    return costs.reduce((acc, curr) => {
        if (coins - curr >= 0) {
            coins -= curr;
            return acc + 1;
        }
        return acc;
    }, 0);
};