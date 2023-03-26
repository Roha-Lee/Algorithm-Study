/**
 * @param {number[]} edges
 * @return {number}
 */
var longestCycle = function(edges) {
    const graph = constructGraph(edges);
    let leaves = collectLeaves(graph);
    while (leaves.length) {
        for (let leaf of leaves) {
            let temp = graph[edges[leaf]];
            temp?.delete(leaf);
            if (temp?.size) {
                graph[edges[leaf]] = temp;
            } else {
                delete graph[edges[leaf]];
            }
        }
        leaves = collectLeaves(graph);
    }
    const arrGraph = [];
    for (let i = 0; i < graph.length; i += 1) {
        if (graph[i] === "#") {
            arrGraph.push(-1);
        } else {
            arrGraph.push(Array.from(graph[i])[0]);
        }
    }
    return findLongestCycle(arrGraph);
};

const constructGraph = (edges) => {
    const graph = { length: edges.length };
    for (let i = 0; i < edges.length; i += 1) {
        if (edges[i] === -1) continue;
        if (!graph[edges[i]]) {
            graph[edges[i]] = new Set([i]);

        } else {
            const temp = graph[edges[i]];
            temp.add(i);
            graph[edges[i]] = temp;
        }
    }
    return graph;
};

const collectLeaves = (graph) => {
    const leaves = [];
    for (let i = 0; i < graph.length; i += 1) {
        if (!graph[i]?.size && graph[i] !== "#") {
            leaves.push(i);
            graph[i] = "#";
        }
    }
    return leaves;
};

const findLongestCycle = (graph) => {
    const traverseCycle = (node, count = 0) => {
        if (node === -1) {
            return count - 1;
        }
        let next = graph[node];
        graph[node] = -1;
        return traverseCycle(next, count + 1);
    };
    let result = -1;
    for (let i = 0; i < graph.length; i += 1) {
        if (graph[i] === -1) continue;
        result = Math.max(traverseCycle(graph[i]), result);
    }
    return result;
};
