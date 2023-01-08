/**
 * @param {number[][]} points
 * @return {number}
 */
function maxPoints(points) {
    return points.reduce((max, p1, index) => {
        const slopeCounter = new Map();
        let samePoint = 0;
        for (let i = index; i < points.length; i += 1) {
            let p2 = points[i];
            if (p1[0] === p2[0] && p1[1] === p2[1]) {
                samePoint += 1;
            } else {
                const slope = p1[0] === p2[0] ? Infinity : (p2[1] - p1[1]) / (p2[0] - p1[0]);
                slopeCounter[slope] = (slopeCounter[slope] || 0) + 1;
            }
        }
        return Math.max(max, samePoint, ...Object.values(slopeCounter).map(count => count + samePoint));
    }, 0);
}
