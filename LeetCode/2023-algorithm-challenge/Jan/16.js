/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    // find location
    const startLocs = intervals.map((item) => item[0]);
    let lowerIndex = findLocation(startLocs, newInterval[0], 0, intervals.length);
    intervals.splice(lowerIndex, 0, newInterval);
    let upperIndex = lowerIndex;
    let insertInterval = newInterval;
    
    // merge left interval
    if (lowerIndex > 0) {
        if (isOverlap(intervals[lowerIndex-1], insertInterval)) {
            lowerIndex -= 1;
            insertInterval = mergeInterval(intervals[lowerIndex], insertInterval);
        }
    }

    // merge right interval
    while (upperIndex < intervals.length && isOverlap(insertInterval, intervals[upperIndex])) {
        insertInterval = mergeInterval(insertInterval, intervals[upperIndex]);
        upperIndex += 1;
    }
    const result = [];
    for (let i = 0; i < lowerIndex; i += 1) {
        result.push(intervals[i]);
    } 
    result.push(insertInterval);
    for (let i = upperIndex; i < intervals.length; i += 1) {
        result.push(intervals[i]);
    }
    return result;
};

const findLocation = (array, val, start, end) => {
    const mid = Math.floor((start + end) / 2);
    if (start > end) return start;
    if (array[mid] > val) {
        return findLocation(array, val, start, mid - 1);
    } else if (array[mid] < val) {
        return findLocation(array, val, mid + 1, end);
    } else {
        return mid;
    }
};
const isOverlap = (int1, int2) => {
    return int1[1] >= int2[0];
}
const mergeInterval = (int1, int2) => {
    return [Math.min(int1[0], int2[0]), Math.max(int1[1], int2[1])];
}
