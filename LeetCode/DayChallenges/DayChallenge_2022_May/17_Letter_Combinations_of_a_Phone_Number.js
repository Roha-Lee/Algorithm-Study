/**
 * @param {string} digits
 * @return {string[]}
 */
 var letterCombinations = function(digits) {
    if(digits.length === 0) return [];
    const map = new Map();
    const numbers = ['2', '3', '4', '5', '6', '7', '8', '9'];
    const letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'];
    const results = [];
    numbers.forEach((num, index) => {
        map.set(num, letters[index]);
    });
    
    /**
     * @param {number} index
     * @param {string} temp
     */
    const dfs = function(index, temp) {
        if(digits.length === index) {
            results.push(temp);
            return;
        }
        const curr = map.get(digits[index]);
        for(let i = 0; i < curr.length; i += 1) {
            dfs(index + 1, temp + curr[i]);
        }
    };

    dfs(0, '');
    return results;
};