/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    const s1Len = s1.length;
    const query = makeCounter(s1);
    const currTemplate = makeCounter(s2.slice(0, s1Len));
    for (let i = s1Len; i < s2.length; i +=1) {
        if (isSame(query, currTemplate)) {
            return true;
        }
        currTemplate[s2[i-s1Len]] -= 1;
        if (currTemplate[s2[i-s1Len]] === 0) {
            delete currTemplate[s2[i-s1Len]];
        }
        currTemplate[s2[i]] = (currTemplate[s2[i]] || 0) + 1;
    }
    return isSame(query, currTemplate);
};

const makeCounter = (string) => {
    const counter = {};
    for (let i = 0; i < string.length; i += 1) {
        counter[string[i]] = (counter[string[i]] || 0) + 1;
    }
    return counter;
}

const isSame = (counter1, counter2) => {
    console.log(counter1, counter2);
    for (const [key, value] of Object.entries(counter1)) {
        if (counter2[key] !== value) {
            return false;
        }
    }
    return true;
}
