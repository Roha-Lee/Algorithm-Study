var SummaryRanges = function() {
    this.array = [Infinity];
};

/** 
 * @param {number} value
 * @return {void}
 */
SummaryRanges.prototype.addNum = function(value) {
    this.array.push(value);
    this.array.sort((a, b) => a - b);
};

/**
 * @return {number[][]}
 */
SummaryRanges.prototype.getIntervals = function() {
    const result = [];
    let lower = -1;
    let prev = -1;
    for (let num of this.array) {
        if (lower === -1) {
            lower = num;
            prev = num;
            continue;
        }
        if (num - prev > 1) {
            result.push([lower, prev]);
            lower = num;
            prev = num;
        } else {
            prev = num;
        }
    }
    return result;
};

/** 
 * Your SummaryRanges object will be instantiated and called as such:
 * var obj = new SummaryRanges()
 * obj.addNum(value)
 * var param_2 = obj.getIntervals()
 */
