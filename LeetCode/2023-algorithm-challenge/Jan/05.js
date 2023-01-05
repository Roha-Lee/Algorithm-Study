/**
 * @param {number[][]} points
 * @return {number}
 */
var findMinArrowShots = function(points) {
    points.sort((a, b) => b[0] - a[0]);
    points.sort((a, b) => b[1] - a[1]);
    let result = 0;
    while(points.length) {
        let threshold = points[points.length-1][1];
        while(points.length && threshold >= points[points.length-1][0]) {
            [start, end] = points.pop();    
        }
        result += 1;    
    }   
    return result;
};