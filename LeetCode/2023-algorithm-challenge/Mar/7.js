/**
 * @param {number[]} time
 * @param {number} totalTrips
 * @return {number}
 */
var minimumTime = function(time, totalTrips) {
    let left = 0;
    let right = 10000000000000000000;
    let totalTime;
    let result = -1;
    while (left <= right) {
        totalTime = Math.floor((left + right)/2);
        if (canSatisfy(time, totalTime, totalTrips)) {
            result = totalTime;
            right = totalTime - 1;
        } else {
            left = totalTime + 1;
        }
    }
    return result;
};

const canSatisfy = (times, totalTime, totalTrips) => {
    return times.reduce((acc, cur) => {
        return acc + Math.floor(totalTime / cur);
    }, 0) >= totalTrips;
}
