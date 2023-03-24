/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minReorder = function(n, connections) {
    const graph = constructGraph(connections);
    const dfs = (node, parent = -1) => {
        let costs = 0;
        for (let [next, canMove] of graph[node]) {
            if (next !== parent) {
                if (!canMove) {
                    costs += 1;
                }
                costs += dfs(next, node); 
            }
        }
        return costs;
    }
    return dfs(0);
};

const constructGraph = (connections) => {
    const graph = {};
    let temp;
    for (let [x, y] of connections) {
        temp = graph[x] || [];
        temp.push([y, false]);
        graph[x] = temp;
        temp = graph[y] || [];
        temp.push([x, true]);
        graph[y] = temp;
    }
    return graph;
};
