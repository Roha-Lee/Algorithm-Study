/**
 * @param {number[]} weights
 * @param {number} days
 * @return {number}
 */
var shipWithinDays = function(weights, days) {
    let left = 0;
    let right = 100000000;
    let mid;
    let result = right;
    while (left <= right) {
        mid = Math.floor((left + right)/2);
        if (isPossible(weights, mid, days)) {
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return result;
};

const isPossible = (weights, maxWeight, days) => {
    let temp = 0;
    for (let i = 0; i < weights.length; i += 1) {
        const curr = weights[i];
        temp += curr;
        if (temp > maxWeight) {
            days -= 1;
            if (days <= 0) {                
                return false;
            }
            temp = curr;
            if (temp > maxWeight) {
                return false;
            }
        }
    }
    return true;
};
