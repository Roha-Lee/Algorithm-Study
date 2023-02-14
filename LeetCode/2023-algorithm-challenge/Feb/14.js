/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    a = "0" + a;
    b = "0" + b;
    a = a.split("").reverse().map(Number);
    b = b.split("").reverse().map(Number);
    while (a.length < b.length) {
        a.push(0);
    }
    while (b.length < a.length) {
        b.push(0);
    }
    let result = new Array(a.length).fill(0);
    carry = 0;
    for (let i = 0; i < a.length; i += 1) {
        add = carry ^ a[i] ^ b[i];
        carry = carry & (a[i] ^ b[i]) | (a[i] & b[i]);
        result[i] = add;
        
    }
    console.log(result, a, b);
    while (result[result.length-1] === 0 && result.length > 1) {
        result.pop();
    }
    return result.map(String).reverse().join("");
};
