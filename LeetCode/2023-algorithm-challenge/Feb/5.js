/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function(s, p) {
    const pLen = p.length;
    const query = makeCounter(p);
    const currTemplate = makeCounter(s.slice(0, pLen));
    const result = [];
    for (let i = pLen; i < s.length; i +=1) {
        if (isSame(query, currTemplate)) {
            result.push(i-pLen);
        }
        currTemplate[s[i-pLen]] -= 1;
        if (currTemplate[s[i-pLen]] === 0) {
            delete currTemplate[s[i-pLen]];
        }
        currTemplate[s[i]] = (currTemplate[s[i]] || 0) + 1;
    }
    if (isSame(query, currTemplate)) {
        result.push(s.length - pLen);
    };
    return result
};

const makeCounter = (string) => {
    const counter = {};
    for (let i = 0; i < string.length; i += 1) {
        counter[string[i]] = (counter[string[i]] || 0) + 1;
    }
    return counter;
};

const isSame = (counter1, counter2) => {
    for (const [key, value] of Object.entries(counter1)) {
        if (counter2[key] !== value) {
            return false;
        }
    }
    return true;
};
