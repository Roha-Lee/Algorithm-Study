/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var minScore = function(n, roads) {
    const graph = generateGraph(roads);
    const visited = new Array(n).fill(false);
    let result = Infinity;
    let queue = [];
    let nextQueue = [1];
    let score;
    while (nextQueue.length) {
        queue = nextQueue;
        nextQueue = [];
        for (let curr of queue) {
            visited[curr] = true;
            for (let next of Object.keys(graph[curr])) {
                if (visited[next]) continue;
                nextQueue.push(next);
                score = graph[curr][next];
                result = Math.min(result, score);
            }
        }
    }
    return result;
};

const generateGraph = (roads) => {
    const graph = {};
    let temp;
    for (let [src, dst, score] of roads) {
        temp = (graph[src] || {});
        temp[dst] = score;
        graph[src] = temp;
        temp = (graph[dst] || {});
        temp[src] = score;
        graph[dst] = temp;
    }
    return graph;
};
