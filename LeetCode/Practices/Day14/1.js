/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
 var backspaceCompare = function(s, t) {
    return operationsToResult(s) === operationsToResult(t);
};

var operationsToResult = function(inputStr) {
    const operations = [];
    for (let char of inputStr) {
        if (char !== "#") operations.push(char);
        if (char === "#" && operations.length > 0) operations.pop();
    }
    return operations.join("");
}