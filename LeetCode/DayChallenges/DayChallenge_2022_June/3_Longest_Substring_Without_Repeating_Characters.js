/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let counter = new Set();
    let maxLength = 0;
    let left = 0;
    for(let right = 0; right < s.length; right += 1) {
        while (counter.has(s[right])) {
            counter.delete(s[left]);
            left += 1;
        }
        maxLength = Math.max(maxLength, right - left + 1);
        counter.add(s[right]);
    }
    return Math.max(maxLength, counter.size);
};