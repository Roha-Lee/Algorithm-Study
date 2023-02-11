/**
 * @param {number} n
 * @param {number[][]} redEdges
 * @param {number[][]} blueEdges
 * @return {number[]}
 */
var shortestAlternatingPaths = function(n, redEdges, blueEdges) {
    const graphs = [generateGraph(redEdges), generateGraph(blueEdges)];
    const results = new Array(n).fill(Infinity);
    for (let startColor of [true, false]) {
        const visited = [new Array(n).fill(false), new Array(n).fill(false)];
        visited[0][0] = true;
        visited[1][0] = true;
        let queue = [0];
        let next = [];
        let curr;
        let isRed = startColor;
        let distance = 0;
        while (queue.length) {
            while (queue.length) {
                curr = queue.pop();
                console.log(curr);
                results[curr] = Math.min(distance, results[curr]);
                if (isRed) {
                    for (let node of (graphs[0][curr] || [])) {
                        if (!visited[0][node]) {
                            visited[0][node] = true;
                            next.push(node);
                        }
                    }
                } else {
                    for (let node of (graphs[1][curr] || [])) {
                        if (!visited[1][node]) {
                            visited[1][node] = true;
                            next.push(node);
                        }
                    }
                }
                console.log(results);
            }
            isRed = !isRed;
            distance += 1;
            queue = next;
            next = [];
        }
    }
    return results.map(item => item === Infinity ? -1 : item);
};

const generateGraph = (edges) => {
    const graph = {};
    for (let i = 0; i < edges.length; i += 1) {
        const [src, dst] = edges[i];
        graph[src] = graph[src] || [];
        graph[src].push(dst);
    }
    return graph;
};
