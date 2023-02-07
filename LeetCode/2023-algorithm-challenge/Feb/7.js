/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function(fruits) {
    let result = 0;
    let left = 0;
    const counter = new Map();
    let kinds = 0;
    for (let right = 0; right < fruits.length; right += 1) {
        const freq = counter.get(fruits[right]) || 0;
        if (freq === 0) {
            kinds += 1;
        }
        counter.set(fruits[right], freq + 1);
        let pastFreq;
        while (kinds > 2) {
            pastFreq = counter.get(fruits[left]) || 0;
            if (pastFreq === 1) {
                kinds -= 1;
            }
            counter.set(fruits[left], pastFreq - 1);
            left += 1;
        }
        if (kinds <= 2) {
            result = Math.max(result, right - left + 1);
        }
    }
    return result;

};
