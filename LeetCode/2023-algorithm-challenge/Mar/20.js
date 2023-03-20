/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    let count = 0;
    for (let i = 0; i < flowerbed.length; i += 1) {
        const left = flowerbed[i-1] || 0;
        const right = flowerbed[i+1] || 0;
        if (left !== 1 && right !== 1 && flowerbed[i] === 0) {
            flowerbed[i] = 1;
            count += 1;
        }
    }
    return count >= n;
};
