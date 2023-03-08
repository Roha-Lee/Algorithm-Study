/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
    let left = 0;
    let right = 10000000000000000000;
    let eatSpeed;
    let result = -1;
    while (left <= right) {
        eatSpeed = Math.floor((left + right)/2);
        if (canSatisfy(piles, eatSpeed, h)) {
            result = eatSpeed;
            right = eatSpeed - 1;
        } else {
            left = eatSpeed + 1;
        }
    }
    return result;
};

const canSatisfy = (piles, eatSpeed, hour) => {
    console.log(piles, eatSpeed, hour);
    return piles.reduce((acc, cur) => {
        return acc + Math.ceil(cur / eatSpeed);
    }, 0) <= hour;
}
