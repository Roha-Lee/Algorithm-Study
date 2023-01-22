/**
 * @param {string} s
 * @return {string[][]}
 */
var partition = function(s) {
    const results = [];
    const n = s.length;
    const temp = [];
    const backtrace = (pos = 0) => {
        if (pos === n) {
            results.push([...temp]);
            return;
        } 
        for (let i = pos + 1; i <= n; i += 1) {
            const substr = s.slice(pos, i);
            if (valid(substr)) {
                temp.push(substr);
                backtrace(i);
                temp.pop();
            }
        }
    }
    backtrace();
    return results;
};

const valid = (s) => {
    const n = s.length;
    for (let i = 0; i < Math.floor(n / 2); i += 1) {
        if (s[i] !== s[n-i-1]) return false;
    } 
    return true;
}
