/**
 * @param {number[]} salary
 * @return {number}
 */
 var average = function(salary) {
    salary.sort((a, b) => a - b);
    return salary.slice(1, salary.length - 1).reduce((a, c) => {
        return a + c;     
    }, 0) / (salary.length - 2);
};