/**
 * @param {number[]} prices
 * @return {number}
 */
 var maxProfit = function(prices) {
    let minPrice = 10001;
    let profit = 0;
    for (let price of prices) {
        if (minPrice > price) {
            minPrice = Math.min(price, minPrice);
        }
        else {
            profit = Math.max(price - minPrice, profit);   
        }
    }
    return profit;
};