/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
 var reverseString = function(s) {
    let left = 0;
    let right = s.length-1;
    let temp;
    while(left < right) {
        temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left += 1;
        right -= 1;
    }
};

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    const words = s.split(' ');
    words.forEach((word, index) => {
        const letters = word.split('');
        reverseString(letters);
        words[index] = letters.join('');
    });
    return words.join(' ');
};