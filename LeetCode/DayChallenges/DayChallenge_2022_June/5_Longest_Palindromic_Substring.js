/**
 * @param {string} s
 * @return {string}
 */
 const longestPalindrome = function(s) {
    let maxLengthString = "";
    for (let center = 0; center < s.length; center += 1) {
        const [left1, right1] = findPalindromeFromLeftRight(s, center, center);
        const [left2, right2] = findPalindromeFromLeftRight(s, center, center + 1);
        if (maxLengthString.length < right1 - left1 + 1) {
            maxLengthString = s.substring(left1, right1 + 1);
        } 
        if (maxLengthString.length < right2 - left2 + 1) {
            maxLengthString = s.substring(left2, right2 + 1);
        }
    }
    return maxLengthString;
};

/**
 * @param {string} s
 * @param {number} left
 * @param {number} right
 * @return {Array[number]}
 */
const findPalindromeFromLeftRight = function(s, left, right) {
    if (s[left] !== s[right]) return [1, 0];
    while (left > 0 && right < s.length - 1 && s[left-1] === s[right+1]) {
        left -= 1;
        right += 1;
    }
    return [left, right];
}