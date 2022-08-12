/**
 * @param {string} s
 * @return {number}
 */
 var longestPalindrome = function(s) {
    const count = {};
    for (let char of s) {
        const curr = count[char];
        count[char] = curr ? curr + 1 : 1;
    }
    let result = 0;
    let oddExist = 0;
    for (let value of Object.values(count)) {
        if (value % 2 !== 0) {
            oddExist = 1;
            result += value - 1;
        }
        else {
            result += value;    
        } 
    }
    return result + oddExist;
};