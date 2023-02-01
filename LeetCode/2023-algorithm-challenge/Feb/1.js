/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    const short = str1.length > str2.length ? str2 : str1;
    const long = str1.length > str2.length ? str1 : str2;
    let gcd = "";
    for (let i = 1; i <= short.length; i += 1) {
        if (short.length % i !== 0 || long.length % i !== 0) {
            continue;
        }
        const shortFactor = short.length / i;
        const longFactor = long.length / i;
        const currGCD = short.slice(0, i);
        if (currGCD.repeat(shortFactor) === short && currGCD.repeat(longFactor) === long) {
            gcd = currGCD;
        }
    }
    return gcd;
};
