/**
 * @param {string} s
 * @return {number}
 */
var minFlipsMonoIncr = function(s) {
    let countOn = false;
    let countOne = 0;
    let countFlip = 0;
    for (let i = 0; i < s.length; i += 1) {
        if (s[i] === "1") {
            countOn = true;
        }
        if (countOn) {
            if (s[i] === "1") {
                countOne += 1;
            } else {
                countFlip += 1;
            }
            countFlip = Math.min(countOne, countFlip);
        }
    }
    return countFlip;
};
