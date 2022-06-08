/**
 * @param {string} s
 * @return {boolean}
 */
 const isPalindrome = function(s) {
    let left = 0;
    let right = s.length - 1;
    while(left <= right) {
        if(s[left++] !== s[right--]) return false;
    }
    return true;
}

/**
 * @param {string} s
 * @return {number}
 */
var removePalindromeSub = function(s) {
    return isPalindrome(s) ? 1 : 2;
};

