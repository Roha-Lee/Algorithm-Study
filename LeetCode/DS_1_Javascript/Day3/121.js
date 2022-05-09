/**
 * @param {number[]} prices
 * @return {number}
 */
 var maxProfit = function(prices) {
    prices.push(0);
    const rev_prices = prices.reverse();
    const result = [];
    let max_price = 0;
    rev_prices.forEach(curr => {
        result.push(Math.max(0, max_price - curr));
        max_price = Math.max(max_price, curr);
    });
    return result.reduce((prev, curr) => Math.max(prev, curr));
};