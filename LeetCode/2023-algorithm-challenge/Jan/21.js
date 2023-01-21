/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    const results = [];
    const n = s.length;
    const temp = [];
    const restore = (pos = 0) => {
        if (temp.length === 4) {
            if (pos !== n) return;
            results.push(arrToIpStr(temp));
            return;
        } 
        for (let i = pos + 1; i <= n; i += 1) {
            const num = s.slice(pos, i);
            if (valid(num)) {
                temp.push(Number(num));
                restore(i);
                temp.pop();
            } else {
                return;
            }
        }
    }
    restore();
    return results;
};

const arrToIpStr = (arr) => arr.join(".");
const valid = (s) => {
    if (s.startsWith('0') && s.length > 1) {
        return false;
    }
    if (0 <= Number(s) && Number(s) <= 255) {
        return true;
    }
    return false;
}
