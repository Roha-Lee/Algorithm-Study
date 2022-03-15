/**
 * @param {string} s
 * @return {string}
 */
 var minRemoveToMakeValid = function(s) {
    let stack = []
    let invalid = [];
    let result = [];
    s.split('').forEach((letter, idx) => {
        if(letter === '(') {
            stack.push(idx)    
        }
        else if(letter === ')') {
            if(stack.length === 0){
                invalid.push(idx)
            }
            stack?.pop()
        }
    })
    console.log(invalid, stack)
    return s.split('').filter((item, idx) => {
        return !(invalid.includes(idx) || stack.includes(idx))
    }).join('')
};