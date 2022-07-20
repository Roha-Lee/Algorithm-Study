/**
 * @param {string} s
 * @param {string[]} words
 * @return {number}
 */
 var numMatchingSubseq = function(s, words) {
    return words.reduce((acc, curr) => {
        return acc + Number(isSubsequence(s, curr));
    }, 0); 
};

const isSubsequence = function(s1, s2) {
    let cur1 = 0;
    let cur2 = 0;
    for (let char of s2) {
        cur1 = s1.indexOf(char, cur1);
        if (cur1 >= 0) {
            cur2 += 1;
            cur1 += 1
        }
    }
    return s2.length === cur2;
};