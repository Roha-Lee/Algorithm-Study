/**
 * @param {number[]} edges
 * @param {number} node1
 * @param {number} node2
 * @return {number}
 */
var closestMeetingNode = function(edges, node1, node2) {
    const mapNodeToDist = new Map();
    let curr = node1;
    let dist = 0;
    const visited = new Array(edges.length).fill(false);
    while (curr !== -1 && !visited[curr]) {
        mapNodeToDist.set(curr, dist);
        visited[curr] = true;
        curr = edges[curr];
        dist += 1;
    }
    
    let currDist = Infinity;
    let result = Infinity;
    curr = node2;
    dist = 0;
    visited.fill(false);
    while (curr !== -1 && !visited[curr]) {
        const pos = mapNodeToDist.get(curr);
        if (Number.isInteger(pos)) {
            const maxDistBetweenNodes = Math.max(pos, dist)
            if (currDist >= maxDistBetweenNodes) {
                if (currDist === maxDistBetweenNodes) {
                    result = Math.min(result, curr);
                } else {
                    result = curr;
                }
                currDist = maxDistBetweenNodes;
            }
        }
        visited[curr] = true;
        curr = edges[curr];
        dist += 1;
    }
    return result === Infinity ? -1 : result;
};
