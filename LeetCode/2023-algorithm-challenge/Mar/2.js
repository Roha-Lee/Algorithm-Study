/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {
    const originalLength = chars.length;
    let count = 1;
    let curr = null;
    let prev = null;
    for (let i = 0; i < originalLength; i += 1) {
        curr = chars.shift();
        if (prev === curr) {
            count += 1;
        } else {
            if (i === 0) {
                prev = curr; 
                continue;
            }
            chars.push(prev);
            if (count > 1) {
                const numArray = Array.from(String(count)).reverse();
                while (numArray.length) {
                    chars.push(numArray.pop());        
                }
            }
            count = 1;
        }
        prev = curr;
    }
    chars.push(prev);
    if (count > 1) {
        const numArray = Array.from(String(count)).reverse();
        while (numArray.length) {
            chars.push(numArray.pop());        
        }
    }
    return chars.length;
};
