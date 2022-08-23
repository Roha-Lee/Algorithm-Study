/**
 * @param {number} n
 * @return {boolean}
 */
 var isHappy = function(n) {
    const numbers = new Set();
    let number;
    numbers.add(n);
    while (true) {
        number = 0;
        for (let char of String(n)) {
            number += Number(char) * Number(char);
        }
        n = number;
        if(number === 1) return true; 
        else if (numbers.has(number)) return false;
        else numbers.add(number);    
    }
};