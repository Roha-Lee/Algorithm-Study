/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function(num, k) {
    let num2 = [];
    let temp = k;
    while (temp > 0) {
        num2.push(temp % 10);
        temp = Math.floor(temp / 10);
    }
    const num1 = num.reverse();
    while (num1.length > num2.length) {
        num2.push(0);
    }
    while (num2.length > num1.length) {
        num1.push(0);
    }
    num1.push(0);
    num2.push(0);
    const result = [];
    let carry = 0;
    for (let i = 0; i < num1.length; i += 1) {
        carry += num1[i] + num2[i];
        result.push(carry % 10);
        carry -= carry % 10;
        carry = Math.floor(carry / 10);
    }
    while (result[result.length-1] === 0) {
        result.pop();
    }
    return result.reverse();
};
