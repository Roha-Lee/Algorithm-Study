/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
 var characterReplacement = function(s, k) {
    
    let left = 0;
    let right=0;
    let map = new Map();
    let res = 0;
    while (right < s.length) {
        map.has(s[right])?map.set(s[right],map.get(s[right])+1):map.set(s[right],1);
        let max = Math.max(...map.values());
        let windowSize = right-left+1;
        if ((windowSize-max) <= k) {
            res = Math.max(res , windowSize);
        }
        while (windowSize-max > k) {
            map.set(s[left],map.get(s[left])-1)
            left++;
            windowSize = right-left+1;
            max = Math.max(...map.values());
        }
        right++;
    }
    return res;
};