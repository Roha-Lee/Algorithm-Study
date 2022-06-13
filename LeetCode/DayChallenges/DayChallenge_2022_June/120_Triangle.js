/**
 * @param {number[][]} triangle
 * @return {number}
 */
 var minimumTotal = function(triangle) {
    return triangle.reverse().reduce((prev, curr) => {
        const next = [];
        curr.forEach((item, index) => {
            next.push(Math.min(item + prev[index], item + prev[index + 1]));    
        });
        return next;
    }, new Array(triangle.length + 1).fill(0))[0];
};